import { createRouter, createWebHashHistory } from "vue-router";

import HomePage from "../components/Home.vue";
import AppProduct from "../components/Product.vue";

const routes = [
    { path: "/", component: HomePage },
    { path: "/product", component: AppProduct },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
