<template>
    <div>
        <h2>Forecast Chart</h2>
        <div>
            <label for="durationInput">Duration (days):</label>
            <input type="number" id="durationInput" v-model="duration" @change="fetchData" min="7" max="365" value="30">
        </div>
        <canvas id="forecastChart"></canvas>
    </div>
</template>
<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
    name: 'ForecastChart',
    data() {
        return {
            chart: null,
            forecastData: [],
            duration: 30
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await axios.get(`/forecast/byWeight?duration=${this.duration}`);
                this.forecastData = response.data;
                this.renderChart();
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        renderChart() {
            if (this.chart) {
                this.chart.destroy();
            }
            const ctx = document.getElementById('forecastChart').getContext('2d');
            this.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.forecastData.points.map(item => item.x),
                    datasets: [{
                        label: 'Forecast',
                        data: this.forecastData.points.map(item => item.y),
                        backgroundColor: 'rgba(255, 206, 86, 0.2)',
                        borderColor: 'rgba(255, 206, 86, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    }
};
</script>

<style scoped>
#forecastChart {
    height: 100%;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
}
</style>