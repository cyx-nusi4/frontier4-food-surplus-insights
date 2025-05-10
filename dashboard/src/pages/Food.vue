<template>
    <div id="food-page">
      <RequestChart />
      <WeightChart />
      <HeatMap />
      <WeightForecastChart />
    </div>
  </template>
  
  <script>
  import HeatMap from '../components/food/WeightHeatmap.vue';
  import RequestChart from '../components/food/RequestsChart.vue';
  import WeightChart from '../components/food/WeightChart.vue';
  import WeightForecastChart from '../components/food/WeightForecastChart.vue';
  
  export default {
    name: 'FoodPage',
    components: {
      HeatMap,
      RequestChart,
      WeightChart,
      WeightForecastChart,
    },
  };
  </script>
  
  <style scoped>
  #food-page {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 10px;
    height: 100vh;
    width: 100vw;
  }
  </style>