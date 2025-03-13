<template>
    <div>
        <h2>Request Chart</h2>
        <canvas id="requestChart"></canvas>
    </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
    name: 'RequestChart',
    data() {
        return {
            chart: null,
            requestData: []
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await axios.get('/requests');
                this.requestData = response.data;
                this.renderChart();
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        renderChart() {
            const ctx = document.getElementById('requestChart').getContext('2d');
            this.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.requestData.requests_points.map(item => item.x),
                    datasets: [{
                        label: 'Requests',
                        data: this.requestData.requests_points.map(item => item.y),
                        backgroundColor: 'rgba(0, 128, 0, 0.2)',
                        borderColor: 'rgba(0, 128, 0, 1)',
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
#requestChart {
    height: 100%;
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
}
</style>