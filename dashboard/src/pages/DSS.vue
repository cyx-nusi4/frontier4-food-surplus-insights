<template>
    <div id="dss-page">
        <RequestsChart class="grid-item" />
        <WeightChart class="grid-item" />
        <RequestsHeatmap class="grid-item" />
        <TimeTrend class="grid-item" />
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
  height: calc(100vh - 90px); /* Adjust for header and paragraph */
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