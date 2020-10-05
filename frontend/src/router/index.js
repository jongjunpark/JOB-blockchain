import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Resume from '../views/Resume.vue'
import ResumeEdit from '../views/ResumeEdit.vue'
import Video from '../views/Video.vue'
import Mypage from '../views/Mypage.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/resume',
    name: 'Resume',
    component: Resume
  },
  {
    path: '/resume/edit',
    name: 'ResumeEdit',
    component: ResumeEdit
  },
  {
    path: '/video',
    name: 'Video',
    component: Video
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
