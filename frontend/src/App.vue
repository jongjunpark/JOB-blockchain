<template>
  <div id="app">
    <div id="nav" v-show="!isLogin">
      <div class="logo-box" @click="goHome">MY RESUME</div>
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
  #nav {
    height: 7vh;
    min-height: 30px;
    background-color: #eff0f5;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    box-shadow: 6px 6px 20px -1px rgba(0,0,0,0.2),
                -6px -6px 20px -1px #ffffff;
    z-index: 5000;
    display: flex;
  }

  #nav .logo-box {
    /* background-color: aqua; */
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Black Han Sans', sans-serif;
    font-weight: 900;
    font-size: calc(0.7vw + 10.5px);
    letter-spacing: -1px;
    cursor: pointer;
    margin: 0 1vw 0 2vw;
    color: #0088ff;
    min-width: 110px;
  }

  #nav .menu-bar-box {
    width: 67%;
    /* background-color: bisque; */
    display: flex;
    align-items: center;
  }

  #nav .user-box {
    width: 20%;
    /* background-color: blueviolet; */
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .menu-bar-box .menu-bar {
    width: calc(3vw + 30px);
    height: 60%;
    /* background-color: cadetblue; */
    margin: 0 1vw;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8vw;
    border-radius: 20px;
    color: rgba(0,0,0,0.8);
    cursor: pointer;
    transition: .3s;
  }

  .menu-bar-box .menu-bar:hover {
    box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
    font-weight: 900;
  }

  .user-box .user-bar {
    width: calc(3vw + 30px);
    height: 60%;
    /* background-color: cadetblue; */
    margin-right: 1vw;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.8vw;
    border-radius: 20px;
    color: rgba(0,0,0,0.8);
    cursor: pointer;
    transition: .3s;
  }

  .user-box .user-bar:hover {
    box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
    font-weight: 900;
  }
</style>
