<template>
  <div id="app">
    
    <RequestChart />
    <WeightChart />
    <HeatMap />
    <WeightForecastChart />
  </div>
</template>

<script>
import HeatMap from './components/HeatMap.vue';
import RequestChart from './components/RequestChart.vue';
import WeightChart from './components/WeightChart.vue';
import WeightForecastChart from './components/WeightForecastChart.vue';
export default {
  name: 'App',
  components: {
    HeatMap,
    RequestChart,
    WeightChart,
    WeightForecastChart,
  }
}
</script>

<style>
#app {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 10px;
  height: 100vh;
  width: 100vw;
}
</style>
