<template>
  <div id="food-page">
    <RequestChart class="grid-item" />
    <WeightChart class="grid-item" />
    <HeatMap class="grid-item" />
    <WeightForecastChart class="grid-item" />
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
  box-sizing: border-box;
  padding: 10px;
}

.grid-item {
  min-width: 0;
  min-height: 0;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: stretch;
  overflow: hidden;
}
</style>