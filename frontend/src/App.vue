<template>
  <div id="app">
    <Dashboard />
    <div class="charts-grid">
      <HeatmapTest />
      <RequestChart />
      <WeightChart />
      <WeightForecastChart />
    </div>
    <router-view/>
  </div>
</template>

<script>
import Dashboard from '@/components/Dashboard.vue';
import HeatmapTest from '@/components/HeatmapTest.vue';
import RequestChart from './components/RequestChart.vue';
import WeightChart from './components/WeightChart.vue';
import WeightForecastChart from './components/WeightForecastChart.vue';

export default {
  name: 'App',
  components: {
    Dashboard,
    HeatmapTest,
    RequestChart,
    WeightChart,
    WeightForecastChart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.charts-grid {
  display: grid;
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2 columns */
  grid-template-rows: repeat(2, 1fr); /* 2 rows */
  gap: 16px; /* Space between charts */
  width: 100%;
  height: 100vh; /* Full viewport height */
  padding: 16px;
  box-sizing: border-box;
  background: #f8f9fa;
}
</style>