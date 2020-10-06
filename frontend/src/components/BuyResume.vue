<template>
  <transition name="modal">
    <div class="buy-search-modal-mask">
      <div class="buy-search-modal-wrap">
        <div class="buy-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='buy-search-modal-header'>이력서를</div>
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
  name: 'BuyResume',
  data() {
    return {
      eth: '',
      password: '',
      private_key: '',
      ans : false,
    }
  },
  watch: {
  },
  props: {
    id: String,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
  },
  mounted() {
    console.log(this.id)
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
    axios.post(`${SERVER_URL}accounts/`, null, config)
        .then((res) => {
          console.log(res.data)
          this.eth = res.data.balance
        })
        .catch(err => {
          console.log(err.response)
        })
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
        "private_key": "0x3951c3125fc62c25fb17d715b576f825e4fcb710e74cfcb139476244a8b260a1"
      }
      axios.post(`${SERVER_URL}accounts/item/${this.id}/`, Data, config)
      .then(res => {
        console.log(res.data)
        if (res.data.result == 'fail') {
          this.ans = true
        } else {
          this.ans = false
        }
      })
      .catch((err) => console.log(err.response))
      let timerInterval
        Swal.fire({
          title: '잠시만 기다려주세요!',
          html: '상품을 구매중입니다',
          timer: 8000,
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
            if (this.ans == true) {
              Swal.fire({
                icon: 'error',
                title: '구매에 실패하였습니다.',
                text: '비밀번호 혹은 서명을 확인해주세요!'
              })} 
            else {
              this.$emit('close')
            }
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