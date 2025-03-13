<template>
    <div>
        <h2>Weight Chart</h2>
        <canvas id="weightChart"></canvas>
    </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
    name: 'WeightChart',
    data() {
        return {
            chart: null,
            weightData: []
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await axios.get('/weights');
                this.weightData = response.data;
                this.renderChart();
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        renderChart() {
            const ctx = document.getElementById('weightChart').getContext('2d');
            this.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.weightData.weight_points.map(item => item.x),
                    datasets: [{
                        label: 'Weight',
                        data: this.weightData.weight_points.map(item => item.y),
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
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
#weightChart {
    height: 100%;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
}
</style>