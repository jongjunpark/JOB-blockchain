<template>
  <div id="app">
    <div v-show="!isLogin">
      <div class="nav" v-if="UserInfo.flag===0">
        <div class="logo-box" @click="goCorpHome">
          <img class="logo-img" src="./assets/logo/B104_logo_basic_skyblue.png" alt="">
        </div>
        <div class="menu-bar-box">
          <div class="menu-bar" @click="goRecruit">공고관리</div>
        </div>
        <div class="user-box">
          <div v-show="isLoggedIn" class="user-name-bar">{{ UserInfo.last_name }}님 환영합니다</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('login')">로그인</div>
          <div v-show="!isLoggedIn" class="user-bar" @click="goLogin('signup')">회원가입</div>
          <div v-show="isLoggedIn" class="user-bar" @click="goLogout">로그아웃</div>
        </div>
      </div>
      <div class="menu-bar-box">
        <div class="menu-bar" @click="goResume">이력서</div>
        <div class="menu-bar">취업달력</div>
        <div class="menu-bar" @click="goVideo">교육</div>
        <div class="menu-bar">검색</div>
      </div>
      <div class="user-box">
        <div v-show="isLoggedIn" class="user-name-bar" @click="goMypage" style="cursor:pointer">{{ UserInfo.last_name }}{{ UserInfo.first_name }}님 환영합니다</div>
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
import { mapState, mapMutations, mapActions } from 'vuex';
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000/';

export default {
  name: 'App',
  data() {
    return {

    }
  },
  mounted() {
    if (this.$cookies.isKey('auth-token')) {
      this.setIsLoggedIn(true);
      this.setToken(this.$cookies.get('auth-token'));
      this.setUserInfo();
    }
    else {
      this.setIsLoggedIn(false);
    }
  },
  methods: {
    ...mapMutations(['setIsLoggedIn', 'setToken', 'setLoginPath', 'setUser']),
    ...mapActions(['setUserInfo']),
    goHome() {
      this.$router.push('/').catch(()=>{})
    },
    goCorpHome() {
      this.$router.push('/corp/recruit').catch(()=>{})
    },
    goResume() {
      this.$router.push('/resume').catch(()=>{})
    },
    goVideo() {
      this.$router.push('/video').catch(()=>{})
    },
    goSearch() {
      this.$router.push('/search').catch(()=>{})
    },
    goRecruit() {
      this.$router.push('/corp/recruit').catch(()=>{})
    },
    goLogin(path) {
      if(path === 'login') {
        this.setLoginPath(path)
      } else {
        this.setLoginPath(path)
      }
      this.$router.push('/login').catch(()=>{})
    },
    goMypage() {
      this.$router.push('/mypage').catch(()=>{})
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
    ...mapState(['isLogin', 'isLoggedIn', 'UserInfo']),
  }
}
</script>