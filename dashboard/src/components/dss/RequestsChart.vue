<template>
  <div>
    <h2 style="text-align: center;">Top 10 DSS by Requests</h2>
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
  name: 'RequestsList',
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
        const response = await fetch('/api/dss/requests')
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
