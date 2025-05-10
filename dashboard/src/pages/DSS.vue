<template>
    <div id="dss-page">
        <RequestsChart class="chart" />
        <WeightChart class="chart" />
        <RequestsHeatmap class="heatmap" />
        <WeightHeatmap class="heatmap" />
    </div>
  </template>
  
<script>
import RequestsHeatmap from '../components/dss/RequestsHeatmap.vue';
import RequestsChart from '@/components/dss/RequestsChart.vue';
import WeightChart from '@/components/dss/WeightChart.vue';
import WeightHeatmap from '@/components/dss/WeightHeatmap.vue';
  
  export default {
    name: 'DSSPage',
    components: {
        RequestsChart,
        RequestsHeatmap,
        WeightChart,
        WeightHeatmap,
    },
  };
  </script>
  
  <style scoped>
  #dss-page {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 10px;
    height: 100vh;
    width: 100vw;
  }
  </style>