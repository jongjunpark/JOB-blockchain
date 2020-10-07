<template>
  <div class='wrap'>
    <div class="wrap-container">
      <div class="schedule-box">
        <div class="recruit-box">
          <p class="recruit-header">추천공고</p>
          <div id="recruit-slider">
            <input type="radio" name='slider' id='recruit-slide1' checked>
            <input type="radio" name='slider' id='recruit-slide2'>
            <input type="radio" name='slider' id='recruit-slide3'>
            <input type="radio" name='slider' id='recruit-slide4'>
            <div id="recruit-controls">
              <label for="recruit-slide1"></label>
              <label for="recruit-slide2"></label>
              <label for="recruit-slide3"></label>
              <label for="recruit-slide4"></label>
            </div>
            <div id="recruit-slides">
              <div id="recruit-overflow">
                <div class="recruit-inner">
                  <div class="recruit-slide slide_1" v-for="(recruitArr,index1) in recruitList2" :key="`recruitArr-${index1}`">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card" v-for="(recruit,index2) in recruitArr" :key="recruit.id" @click="onModal(recruit.id,'individual')">
                          <div class="recruit-card-img-box">
                            <img :src="'http://localhost:8000'+recruitImg2[index1*5+index2]" alt="">
                          </div>
                          <p>{{ recruit.user.last_name }}</p>
                          <p>{{ recruit.title }}</p>
                          <p>~ {{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}
                             {{recruit.deadline.substring(8,10)}}:{{recruit.deadline.substring(10,)}}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          
        </div>
      </div>
      <div class="schedule-box">
        <div class="test-box">
          <p class="test-header">마감임박 공고</p>
          <div id="test-slider">
            <input type="radio" name='slider2' id='test-slide1' checked>
            <input type="radio" name='slider2' id='test-slide2'>
            <input type="radio" name='slider2' id='test-slide3'>
            <input type="radio" name='slider2' id='test-slide4'>
            <div id="test-controls">
              <label for="test-slide1"></label>
              <label for="test-slide2"></label>
              <label for="test-slide3"></label>
              <label for="test-slide4"></label>
            </div>
            <div id="test-slides">
              <div id="test-overflow">
                <div class="test-inner">
                  <div class="test-slide slide_1" v-for="(recruitArr,index1) in recruitList" :key="`recruitArr-${index1}`">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card" v-for="(recruit,index2) in recruitArr" :key="recruit.id" @click="onModal(recruit.id,'individual')">
                          <div class="test-card-img-box">
                            <img :src="'http://localhost:8000'+recruitImg[index1*5+index2]" alt="">
                          </div>
                          <p>{{ recruit.user.last_name }}</p>
                          <p>{{ recruit.title }}</p>
                          <p>~ {{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}
                             {{recruit.deadline.substring(8,10)}}:{{recruit.deadline.substring(10,)}}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          
        </div>
      </div>
    </div>

    <RecruitModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios'
import { mapMutations } from 'vuex';
import RecruitModal from '../components/RecruitModal.vue'
import '../components/css/home.css'

const SERVER_URL = 'http://127.0.0.1:8000/'
// const WORK_API_KEY = process.env.VUE_APP_WORK_API_KEY

export default {
  name: 'Home',
  data() {
    return {
      showModal: false,
      recruitImg: [],
      recruitImg2: [],
      recruitList: [],
      recruitList2: [],
    }
  },
  components: {
    RecruitModal
  },
  mounted() {
    this.getRecruit()
    this.getRecruit2()
  },
  methods: {
    ...mapMutations(['setUserDivide', 'setRecruitId']),
    onModal(id, type) {
      this.setRecruitId(id)
      this.setUserDivide(type)
      this.showModal = true;
    },
    getRecruit() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/showlist/`, null, config)
      .then(res => {
        console.log(res,'get showlist')
        if(res.data.length>5) {
          for(let j=0; j<res.data.length/5; j++){
            let ARR = []
            for(let i=0; i<5; i++) {
              if(res.data.length<=j*5+i){
                break
              } else {
                ARR.push(res.data[j*5+i])
              }
            }
            this.recruitList.push(ARR)
          } 
        } else {
          let ARR = []
          for(let i=0; i<res.data.length; i++) {
              ARR.push(res.data[i])
          }
          this.recruitList.push(ARR)
        }
        for(let i=0; i<res.data.length; i++) {
          axios.get(`${SERVER_URL}articles/${res.data[i].user.id}/`, null, config)
          .then(response => {
            this.recruitImg.push(response.data.image)
          })
          .catch((err) => console.log(err.response))
        }
      })
      .catch((err) => console.log(err.response))
    },
    getRecruit2() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/showlist2/`, null, config)
      .then(res => {
        console.log(res,'get showlist2')
        if(res.data.length>5) {
          for(let j=0; j<res.data.length/5; j++){
            let ARR = []
            for(let i=0; i<5; i++) {
              if(res.data.length<=j*5+i){
                break
              } else {
                ARR.push(res.data[j*5+i])
              }
            }
            this.recruitList2.push(ARR)
          } 
        } else {
          let ARR = []
          for(let i=0; i<res.data.length; i++) {
              ARR.push(res.data[i])
          }
          this.recruitList2.push(ARR)
        }
        for(let i=0; i<res.data.length; i++) {
            axios.get(`${SERVER_URL}articles/${res.data[i].user.id}/`, null, config)
            .then(response => {
              this.recruitImg2.push(response.data.image)
            })
            .catch((err) => console.log(err.response))
        }
      })
      .catch((err) => console.log(err.response))
    }
    // getRecruitInform() {
    //   console.log(WORK_API_KEY)
    //   axios.get('http://openapi.work.go.kr/opi/opi/opia/wantedApi.do', {
    //     params: {
    //       authKey: WORK_API_KEY,
    //       callTp: 'L',
    //       returnType: 'XML',
    //       startPage: 1,
    //       display: 10,
    //       coTp: '01'
    //     }
    //   }).then(res => {
    //     console.log(res)
    //   })
    //   .catch(err =>{
    //     console.log(err.response)
    //   })
    // }
  }
}
</script>