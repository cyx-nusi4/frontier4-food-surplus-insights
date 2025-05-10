<template>
    <div>
        <h2>Future Food Weight Forecast</h2>
        <div style="text-align: right;">
            <label for="durationInput">Duration (days):</label>
            <input type="number" id="durationInput" v-model.number="duration" @change="fetchData" min="7" max="365">
        </div>
        <div style="width: 600px; height: 400px;">
            <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
            <div v-else>Loading chart data...</div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const loaded = ref(false);
const duration = ref(30);
const chartData = ref({
    labels: [],
    datasets: [{
        label: 'Forecast by Weight',
        data: [],
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
    }]
});

const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        title: {
            display: true,
            text: `Forecast for Next ${duration.value} Days`
        }
    },
    scales: {
        y: {
            beginAtZero: true,
            title: {
                display: true,
                text: 'Weight (kg)'
            }
        },
        x: {
            title: {
                display: true,
                text: 'Date'
            }
        }
    }
});

const fetchData = async () => {
    try {
        loaded.value = false;
        const response = await axios.get(`/api/forecast/byWeight?duration=${duration.value}`);
        const forecastData = response.data;
        
        chartData.value.labels = forecastData.points.map(item => item.x);
        chartData.value.datasets[0].data = forecastData.points.map(item => item.y);
        
        // Update chart title with current duration
        chartOptions.value.plugins.title.text = `Forecast for Next ${duration.value} Days`;
        
        loaded.value = true;
    } catch (error) {
        console.error('Error fetching data:', error);
        loaded.value = false;
    }
};

onMounted(fetchData);
</script>

<style scoped>
input[type="number"] {
    margin: 0 10px;
    padding: 5px;
    width: 60px;
}
div[style*="width: 600px; height: 400px;"] {
    margin: 0 auto;
}
h2 {
    text-align: center;
}
</style>