import { createRouter, createWebHistory } from 'vue-router'
import ZipInput from '../components/ZipInput.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ZipInput
    }
  ]
})

export default router
