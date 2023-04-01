import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

// Set axios default configurations
axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.headers.common['Content-Type'] = 'application/json';

const app = createApp(App);

// Add axios to app instance for easy access throughout the application
app.config.globalProperties.$axios = axios;

app.use(router);
app.use(store);
app.mount('#app');
