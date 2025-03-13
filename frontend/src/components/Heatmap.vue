<!-- <template>
    <div>
        <label for="start-date">Start Date:</label>
        <input type="date" id="start-date" v-model="startDate" value="2024-01-01">
        
        <label for="end-date">End Date:</label>
        <input type="date" id="end-date" v-model="endDate" value="2024-12-31">
        
        <button @click="fetchHeatmapData">Update Heatmap</button>
        
        <div id="heatmap"></div>
    </div>
    <GoogleMap
        api-key="YOUR_GOOGLE_MAPS_API_KEY"
        :libraries="['visualization']"
        style="width: 100%; height: 500px"
        :center="sanFrancisco"
        :zoom="13"
    >
        <HeatmapLayer :options="{ data: heatmapData }" />
    </GoogleMap>
</template>

<script>
    import axios from 'axios';
    import { GoogleMap, HeatmapLayer } from 'vue3-google-map'

    const sanFrancisco = { lat: 37.774546, lng: -122.433523 };
    const heatmapData = [
        { location: { lat: 37.782, lng: -122.447 }, weight: 0.5 },
        { lat: 37.782, lng: -122.445 },
        { location: { lat: 37.782, lng: -122.443 }, weight: 2 },
        { location: { lat: 37.782, lng: -122.441 }, weight: 3 },
        { location: { lat: 37.782, lng: -122.439 }, weight: 2 },
        { lat: 37.782, lng: -122.437 },
        { location: { lat: 37.782, lng: -122.435 }, weight: 0.5 },

        { location: { lat: 37.785, lng: -122.447 }, weight: 3 },
        { location: { lat: 37.785, lng: -122.445 }, weight: 2 },
        { lat: 37.785, lng: -122.443 },
        { location: { lat: 37.785, lng: -122.441 }, weight: 0.5 },
        { lat: 37.785, lng: -122.439 },
        { location: { lat: 37.785, lng: -122.437 }, weight: 2 },
        { location: { lat: 37.785, lng: -122.435 }, weight: 3 },
    ];
</script>

<style scoped>
#heatmap {
    height: 100%;
    width: 100%;
}
</style> -->