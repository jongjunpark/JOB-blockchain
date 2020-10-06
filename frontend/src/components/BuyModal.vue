<template>
  <transition name="modal">
    <div class="buy-search-modal-mask">
      <div class="buy-search-modal-wrap">
        <div class="buy-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='buy-search-modal-header'>영상을</div>
          <div class='buy-search-modal-header'>구매하시겠습니까?</div>
          <div class="buy-modal-buy">
            가격 : <p class="price">1000000 (ETH)</p>
          </div>
          <div class="buy-modal-buy">
            수수료 : <p class="price">121000 (gas)</p>
          </div>
          <div class="buy-modal-buy">
            내 잔액 : <p class="price-eth">{{ eth }} (ETH)</p>
          </div>
          <div class="buyVideoActive" v-if="eth>1000000+121000" @click="goBuy">구매하기</div>
          <div class="buyVideoNoactive" v-else>구매하기</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import './css/buymodal.css'
import { mapState } from 'vuex';
import axios from 'axios';
import Swal from 'sweetalert2'
const SERVER_URL = 'http://127.0.0.1:8000/'



export default {
  name: 'BuyModal',
  props: {
    videoName: String,
  },

  data() {
    return {
      eth: '',
      password: '',
      private_key: '',
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  mounted() {
    this.eth = this.UserInfo.balance
    console.log(this.UserInfo)
  },
  methods: {
    goBuy() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const Data = {
        "password": "qhdrb111",
        "private_key": "0xfc99bd02ff720fa73bb3d5772806a14573cd59dfda9af34704ab1d42bbf573e3",
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