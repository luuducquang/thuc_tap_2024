import { createRouter, createWebHistory } from 'vue-router';

import DefaultLayout from '@/layouts/DefaultLayout.vue';

import Home from '@/views/Home.vue';
import Product from '@/views/Product.vue';

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
        meta: {
          breadcrumbName: 'Home'
        }
      },
      {
        path: 'product',
        name: 'Product',
        component: Product,
        meta: {
          breadcrumbName: 'Product'
        }
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
