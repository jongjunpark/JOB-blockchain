<template>
  <div class="wrap">
    <div class="wrap-container">
      <input type="file" id="default" accept="image/*" @change="setProfileImg">
      <div @click="tested">ㅎㅇ</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'RecruitWrite',
  data() {
    return {
      test: '',
      img: '',
    }
  },
  components: {
  },
  computed: {
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
  },
  watch: {
  },
  methods: {
    handleScroll() {
      console.log('Base')
    },
    setProfileImg() {
      var photoFile = document.getElementById("default");
      console.log(photoFile.files[0],'dqwqwd')
      this.img = photoFile.files[0]
    },
    tested() {
      let data = new FormData();
      data.append('image', this.img);
      for (var key of data.keys()) {console.log(key);}
      for (var value of data.values()) {console.log(value);}
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.put(`${SERVER_URL}articles/1/`, data, config)
      .then(res => {
        console.log(res)
      })
      .catch((err) => console.log(err.response))
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>

</style>