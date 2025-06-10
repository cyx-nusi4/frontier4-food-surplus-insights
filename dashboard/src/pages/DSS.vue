<template>
    <h2 style="text-align: center;">DSS Overview</h2>
    <p>This page provides an overview of the DSS insights.</p>
    <div id="dss-page">
        
        <RequestsChart class="chart" />
        <WeightChart class="chart" />
        <RequestsHeatmap class="heatmap" />
        <!-- <WeightHeatmap class="heatmap" /> -->
        <!-- <DistributionChart class="chart" /> -->
        <TimeTrend class ="chart" />
        <div class="chart" style="grid-column: span 2; grid-row: span 2;">
            
        </div>
    </div>
  </template>
  
<script>
import RequestsHeatmap from '../components/dss/RequestsHeatmap.vue';
import RequestsChart from '@/components/dss/RequestsChart.vue';
import WeightChart from '@/components/dss/WeightChart.vue';
// import WeightHeatmap from '@/components/dss/WeightHeatmap.vue';
// import DistributionChart from '@/components/dss/DistributionChart.vue'
import TimeTrend from '@/components/dss/TimeTrend.vue';
  
  export default {
    name: 'DSSPage',
    components: {
        RequestsChart,
        RequestsHeatmap,
        WeightChart,
        // WeightHeatmap,
        // DistributionChart,
        TimeTrend,
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