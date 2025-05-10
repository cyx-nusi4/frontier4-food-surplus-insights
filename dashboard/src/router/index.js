import { createRouter, createWebHistory } from 'vue-router';
import Food from '../pages/Food.vue';
import DSS from '../pages/DSS.vue';

const routes = [
  { path: '/', redirect: '/food' },
  { path: '/food', component: Food },
  { path: '/dss', component: DSS },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;