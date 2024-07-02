import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import Andt from'ant-design-vue'

const app = createApp(App);
app.use(router);
app.use(Andt);
app.mount('#app');
