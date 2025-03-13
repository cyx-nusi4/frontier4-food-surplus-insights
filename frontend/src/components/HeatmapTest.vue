<template>
  <div>
    <div>
      <h2> heatmap test</h2>
    </div>
    <GmapMap
      :center="sanFrancisco"
      :zoom="13"
      style="width: 100%; height: 500px"
    >
      
    </GmapMap>
    <GmapHeatmapLayer :data="heatmapData" :options="heatmapOptions"/>
  </div>

</template>

<script>
import { GmapMap, GmapHeatmapLayer } from 'vue2-google-maps'

export default {
  name: 'HeatmapTest',
  components: {
    GmapMap,
    GmapHeatmapLayer,
  },
  data() {
    return {
      sanFrancisco: { lat: 37.774546, lng: -122.433523 },
      heatmapData: [
        { lat: 37.782, lng: -122.447, weight: 0.5 },
        { lat: 37.782, lng: -122.443, weight: 2 },
        { lat: 37.782, lng: -122.441, weight: 3 },
        { lat: 37.782, lng: -122.439, weight: 2 },
        { lat: 37.782, lng: -122.435, weight: 0.5 },
        { lat: 37.785, lng: -122.447, weight: 3 },
        { lat: 37.785, lng: -122.445, weight: 2 },
        { lat: 37.785, lng: -122.441, weight: 0.5 },
        { lat: 37.785, lng: -122.437, weight: 2 },
        { lat: 37.785, lng: -122.435, weight: 3 },
      ], 
      heatmapOptions: {
        dissipating: false,
        radius: 20,
      },
    }
  },
}
</script>