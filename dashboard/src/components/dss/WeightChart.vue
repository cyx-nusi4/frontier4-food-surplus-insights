<template>
  <div class="weight-chart">
    <h2>Top 10 DSS by Food Weight</h2>
    <ul v-if="loaded">
      <li v-for="(item, index) in limitedData" :key="index">
        {{ item.x }}: {{ item.y }}
      </li>
    </ul>
    <div v-else>Loading data...</div>
  </div>
</template>

<script>
export default {
  name: 'WeightChart',
  data() {
    return {
      loaded: false,
      dataPoints: [],
    }
  },
  computed: {
    limitedData() {
      return this.dataPoints.slice(0, 10)
    }
  },
  async mounted() {
    await this.fetchData()
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('/api/dss/weight')
        const data = await response.json()

        // Process the data
        this.dataPoints = data.points
        this.loaded = true
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }
  }
}
</script>

<style scoped>
.weight-chart {
  text-align: center;
  font-family: Arial, sans-serif;
  font-size: 14px;
}
.weight-chart h2 {
  font-size: 24px;
  margin-bottom: 10px;
}
.weight-chart ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  display: inline-block;
  text-align: left;
}
.weight-chart li {
  font-size: 14px;
}
</style>
