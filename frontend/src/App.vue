<template>
  <div id="app">
    <div id="nav" v-show="!isLogin">
      <div class="logo-box" @click="goHome">
        <img class="logo-img" src="./assets/logo/B104_logo_basic_skyblue.png" alt="">
      </div>
      <div class="menu-bar-box">
        <div class="menu-bar" @click="goResume">이력서</div>
        <div class="menu-bar">취업달력</div>
        <div class="menu-bar">교육</div>
        <div class="menu-bar">검색</div>
      </div>
      <div class="user-box">
        <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('login')">로그인</div>
        <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('signup')">회원가입</div>
        <div v-show="isLoggedIn" class="user-bar" @click="goLogout">로그아웃</div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import "../public/css/common.css";
import { mapState, mapMutations } from 'vuex';
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000/';

export default {
  name: 'App',
  data() {
    return {

    }
  },
  methods: {
    ...mapMutations(['setIsLoggedIn', 'setToken', 'setLoginPath']),
    goHome() {
      this.$router.push('/').catch(()=>{})
    },
    goResume() {
      this.$router.push('/resume').catch(()=>{})
    },
    goLogin(path) {
      if(path === 'login') {
        this.setLoginPath(path)
      } else {
        this.setLoginPath(path)
      }
      this.$router.push('/login').catch(()=>{})
    },
    goLogout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(`${SERVER_URL}rest-auth/logout/`, null, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.setToken(null)
          this.setIsLoggedIn(false)
          // if (this.$route.name === 'Home') {
          //   this.$router.go(this.$router.currentRoute)
          // } else {
          //   this.$router.push('/')
          // }
          this.$router.push('/').catch(()=>{})
        })
        .catch(err => {
          console.log(err.response)
        })
    }
  },
  computed: {
    ...mapState(['isLogin', 'isLoggedIn']),
  }
}
</script>

<style>
  
</style>
