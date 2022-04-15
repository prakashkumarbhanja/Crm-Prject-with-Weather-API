import { createRouter, createWebHashHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import SignUp from '@/views/SignUp.vue'
import Login from '@/views/Login.vue'
import Dashboard from '@/views/dashboard/Dashboard.vue'
import MyAccount from '@/views/dashboard/MyAccount.vue'
import Leads from '@/views/dashboard/Leads.vue'
import Lead from '@/views/dashboard/Lead.vue'
import AddLead from '@/views/dashboard/AddLead.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: Leads,
    meta:{
      requireLogin: true
    }
  },
  
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: Lead,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLead,
    meta:{
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
