<template>
    <div>
        <h2 style="text-align: center;">Food Collected Heatmap</h2>
        <div id="map"></div>
        <div v-if="loading" class="loading-message">Loading heatmap data...</div>
        <div v-if="error" class="error-message">Error loading heatmap: {{ error }}</div>
    </div>
</template>

<script>
import { Loader } from '@googlemaps/js-api-loader';
import axios from 'axios';

export default {
    name: 'HeatMap',
    data() {
        return {
            map: null,
            heatmap: null,
            singapore: { lat: 1.3521, lng: 103.8198 },
            heatmapData: [],
            loading: false,
            error: null,
            googleMaps: null // Store the google object here
        };
    },
    mounted() {
        this.initMap();
    },
    methods: {
        async initMap() {
            this.loading = true;
            this.error = null;
            
            try {
                // Initialize Google Maps
                const loader = new Loader({
                    apiKey: process.env.VUE_APP_GOOGLE_MAPS_API_KEY,
                    libraries: ['visualization'],
                    version: 'weekly'
                });
                console.log(process.env.VUE_APP_GOOGLE_MAPS_API_KEY);

                // Store the google object when loaded
                this.googleMaps = await loader.load();
                
                // Create the map
                this.map = new this.googleMaps.maps.Map(document.getElementById('map'), {
                    center: this.singapore,
                    zoom: 11,
                    mapTypeId: 'roadmap'
                });

                // Fetch heatmap data from API
                await this.fetchHeatmapData();
                
            } catch (e) {
                console.error('Error initializing map:', e);
                this.error = 'Failed to initialize map. Please try again later.';
            } finally {
                this.loading = false;
            }
        },
        
        async fetchHeatmapData() {
            if (!this.googleMaps) return;
            
            try {
                this.loading = true;
                const response = await axios.get('/api/heatmap');
                const rawData = response.data.heat_data;
                
                // Transform API data to Google Maps format
                this.heatmapData = rawData.map(point => ({
                    location: new this.googleMaps.maps.LatLng(point[0], point[1]),
                    weight: point[2]
                }));
                
                // Create or update heatmap layer
                if (this.heatmap) {
                    this.heatmap.setData(this.heatmapData);
                } else {
                    this.heatmap = new this.googleMaps.maps.visualization.HeatmapLayer({
                        data: this.heatmapData,
                        map: this.map,
                        radius: 20,
                        dissipating: true
                    });
                }
                
                // Adjust viewport to contain all points if needed
                if (this.heatmapData.length > 0) {
                    const bounds = new this.googleMaps.maps.LatLngBounds();
                    this.heatmapData.forEach(point => bounds.extend(point.location));
                    this.map.fitBounds(bounds);
                }
                
            } catch (e) {
                console.error('Error fetching heatmap data:', e);
                this.error = 'Failed to load heatmap data.';
            } finally {
                this.loading = false;
            }
        }
    }
};
</script>

<style scoped>
#map {
    height: 400px;
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.loading-message, .error-message {
    text-align: center;
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
}

.loading-message {
    background-color: #f8f9fa;
    color: #6c757d;
}

.error-message {
    background-color: #f8d7da;
    color: #721c24;
}
</style>
