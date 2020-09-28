import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Resume from '../views/Resume.vue'
import ResumeEdit from '../views/ResumeEdit.vue'
import Video from '../views/Video.vue'
import RecruitHome from '../views/RecruitHome.vue'
import RecruitWrite from '../views/RecruitWrite.vue'

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
    path: '/corp/recruit',
    name: 'RecruitHome',
    component: RecruitHome
  },
  {
    path: '/corp/recruit/write',
    name: 'RecruitWrite',
    component: RecruitWrite
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
