<template>
  <transition name="modal">
    <div class="mail-modal-mask">
      <div class="mail-modal-wrap">
        <div class="mail-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div>
            <h1>서멍해주세요</h1>
            <input v-model="password" placeholder="비밀번호를 입력하세요">
            <h1>개인키를 입력하세요</h1>
            <input v-model="key">
          </div>
          <button @click="goBuy">확인</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import './css/mail-validation-modal.css'
import Swal from 'sweetalert2'
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'SignModal.vue',
  data(){
    return {
      password: '',
      key: '',
    }
  },
  methods: {
    goBuy() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const Data = {
        "password": this.password,
        "private_key": this.key,
        "video": this.videoName
      }
      axios.post(`${SERVER_URL}accounts/video/${this.UserInfo.id}/`, Data, config)
      .then(res => {
        console.log(res.data)
      })
      .catch((err) => console.log(err.response))
      let timerInterval
          Swal.fire({
            title: '잠시만 기다려주세요!',
            html: '상품을 구매중입니다',
            timer: 7000,
            timerProgressBar: true,
            showConfirmButton: false,
            willOpen: () => {
              Swal.showLoading()
              timerInterval = setInterval(() => {
                const content = Swal.getContent()
                if (content) {
                  const b = content.querySelector('b')
                  if (b) {
                    b.textContent = Swal.getTimerLeft()
                  }
                }
              }, 100)
            },
            onClose: () => {
              clearInterval(timerInterval)
            }
          }).then((result) => {
            /* Read more about handling dismissals below */
            if (result.dismiss === Swal.DismissReason.timer) {
              console.log('I was closed by the timer')
              this.$router.go('/video')
            }
            // <int:article_pk>/certificates/create
            // this.createCertificate()
            // this.createLang()
            // this.createCareer()
          })
    }
  },
}
</script>

<style>

</style>