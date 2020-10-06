import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Video from '../views/Video.vue'
import Resume from '../views/Resume.vue'
import ResumeEdit from '../views/ResumeEdit.vue'
import RecruitHome from '../views/RecruitHome.vue'
import RecruitWrite from '../views/RecruitWrite.vue'
import Applicant from '../views/Applicant.vue'
import Mypage from '../views/Mypage.vue'
import Search from '../views/Search.vue'

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
  },
  {
    path: '/corp/recruit/applicant/:recruitID',
    name: 'Applicant',
    component: Applicant
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
