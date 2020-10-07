<template>
  <div class="wrap">
    <div class="wrap-container search-container">
      <img src="../assets/logo/B104_logo_border.png" alt="#" class="search-logo">
      <div class="search-user-box">
        <input type="text" class="search-input" placeholder="유저이름을 검색하세요" v-model="username" v-on:input="username = $event.target.value">
          <transition-group v-show="username" name='fade' tag="div" class="search-user-group" mode="in-out">
            <p v-if="userList.length===0" key='-1'>검색결과가 없습니다.</p>
            <div class='search-user-item' v-for='user in userList' :key='user.user.id' @click="onModal(user.user.id, 'search')">
              <div class="search-user-img">
                <img v-show="user.image" :src="'https://j3b104.p.ssafy.io/' + user.image" alt="#">
                <img v-show="!user.image" src="../assets/images/default-user.png" alt="#">
              </div>
              <div class="search-user-content">
                <div class="search-user-name">{{ user.name }}</div>
              </div>
            </div>
            <!-- <div v-show="userListLength > 0" class='search-user-more' key='0'>{{ userListLength }}개 더보기</div> -->
          </transition-group>
      </div>
    </div>

    <UserModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios';
import UserModal from '../components/UserModal.vue';
import { mapMutations } from 'vuex';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Search',
  data() {
    return {
      username: '',
      userList: [],
      userListLength: 0,
      showModal: false,
    }
  },
  components: {
    UserModal,
  },
  computed: {
  },
  mounted() {
  },
  watch: {
    username() {
      if (this.username) {
        this.searchUser()
      }
    }
  },
  methods: {
    ...mapMutations(['setUserModalId', 'setUserDivide']),
    searchUser() {
      console.log(this.username)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}articles/search/${this.username}/`, null, config)
      .then(res => {
        console.log(res,'get search')
        if(res.data) {
          this.userList = res.data
        } else {
          this.userList = []
        }
      })
      .catch((err) => console.log(err.response))
    },
    onModal(id, type) {
      this.setUserModalId(id);
      this.setUserDivide(type)
      this.showModal = true;
    },
  },
}
</script>

<style>
.search-container .search-logo {
  width: 15%;
  margin-top: 100px;
}

.search-container .search-user-box {
  position: relative;
}

.search-user-box input {
  width: 500px;
  height: 40px;
  padding-left: 25px;
  padding-right: 25px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border: none;
  border-radius: 20px;
  outline: none;
  background: transparent;
  margin-top: 20px;
}

.search-user-group {
  position: absolute;
  top: 65px;
  left: 50%;
  transform: translate(-50%, 0);
  width: 98%;
  padding: 1%;
  border-radius: 10px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
}

.search-user-group > p {
  font-size: 12px;
  color: rgba(0,0,0,0.8);
  margin: 5px 0;
}

.search-user-group .search-user-item {
  width: 100%;
  height: 50px;
  display: flex;
  cursor: pointer;
  padding: 30px 10px;
  transition: all 0.2s ease;
  box-sizing: border-box;
  /* box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff; */
  border-radius: 10px;
}

.search-user-group .search-user-item:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  background-color: #ececf0 !important;
}

.search-user-group .search-user-more {
  width: 100%;
  height: 3.5vh;
  font-size: 1.8vh;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  color: black;
}

.search-user-item .search-user-img {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 10px;
}

.search-user-img img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
}

.search-user-item .search-user-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  width: 100%;
}

.search-user-content .search-user-name {
  font-size: 15px;
  display: flex;
  align-items: center;
  font-weight: 500;
  height: 50%;
  width: 100%;
  color: rgba(0,0,0,0.8)
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s !important;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>