<template>
    <div>
        <h2>DSS Time Trend</h2>
        <!-- <div style="text-align: right;">
            <label for="durationInput">Duration (days):</label>
            <input type="number" id="durationInput" v-model.number="duration" @change="fetchData" min="7" max="365">
        </div> -->
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
// const duration = ref(30);
const chartData = ref({
    labels: [],
    datasets: [{
        label: 'DSS in service',
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

    },
    scales: {
        y: {
            beginAtZero: true,
            title: {
                display: true,
                text: 'Count'
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
        const response = await axios.get(`/api/dss/time-trend`);
        const forecastData = response.data;
        
        chartData.value.labels = forecastData.data.map(item => item.date);
        chartData.value.datasets[0].data = forecastData.data.map(item => item.count);
        
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