<template>
    <div>
      <h2 style="text-align: center;">Food Collected by Location</h2>
      <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
      <div v-else>Loading chart data...</div>
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'WeightChart',
    components: { Bar },
    data() {
      return {
        loaded: false,
        chartData: {
          labels: [],
          datasets: [
            {
              label: 'weight',
              backgroundColor: '#4e73df',
              data: []
            }
          ]
        },
        chartOptions: {
          responsive: true,
          plugins: {
            legend: {
              display: true,
              position: 'top'
            },
            // title: {
            //   display: true,
            //   text: 'Recovered Food Weight by Location'
            // }
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Weight'
              }
            },
            x: {
              title: {
                display: true,
                text: 'Location'
              }
            }
          }
        }
      }
    },
    async mounted() {
      await this.fetchData()
    },
    methods: {
      async fetchData() {
        try {
          const response = await fetch('/api/food/weight')
          const data = await response.json()
          
          // Process the data
          this.chartData.labels = data.points.map(item => item.x)
          this.chartData.datasets[0].data = data.points.map(item => item.y)
          
          this.loaded = true
        } catch (error) {
          console.error('Error fetching chart data:', error)
        }
      }
    }
  }
  </script>