import { createRouter, createWebHistory } from 'vue-router';
import Register from './views/Register.vue';
import Login from './views/Login.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    // Add your other routes here
  ],
});

export default router;
