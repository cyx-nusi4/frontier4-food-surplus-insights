import Vue from 'vue'
import App from './App.vue'
import router from './router';
import * as VueGoogleMaps from 'vue2-google-maps';

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAU_U6QQDLM4hw73oe_YHNkZL5Jm9IF02o', // Replace with your Google Maps API key
    libraries: 'visualization', // Necessary for heatmap
  },
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')