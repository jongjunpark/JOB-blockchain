<template>
  <div class='wrap'>
    <div class="wrap-container home-container">
      <div class="schedule-box">
        <div class="recruit-box">
          <p class="recruit-header">마감임박 공고</p>
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
                  <div class="recruit-slide slide_1" v-for="(recruitArr,index1) in recruitList" :key="`recruitArr-${index1}`">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card" v-for="(recruit,index2) in recruitArr" :key="recruit.id" @click="onModal(recruit.id,'individual')">
                          <div class="recruit-card-img-box">
                            <img :src="'http://localhost:8000'+recruitImg[index1*3+index2]" alt="">
                          </div>
                          <p>{{ recruit.user.last_name }}</p>
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
      selectYear: '',
      selectMonth: '',
      selectDay: '',
      isSelect: false,
      defaultSchedule: {
        200916 : {
          recruit: ['네이버', '삼성전자'],
          test: ['제49회 SQLD', '기사 제4회 실기시험'],
        },
        200917 : {
          recruit: ['네이버', '삼성전자'],
          test: ['제49회 SQLD', '기사 제4회 실기시험'],
        },
        200918 : {
          recruit: ['네이버', '삼성전자'],
          test: ['제49회 SQLD', '기사 제4회 실기시험'],
        },
        200930 : {
          recruit: ['삼성전자', '카카오'],
          test: ['기사 제4회 실기시험'],
        },
      },
      todayRecruits: [],
      todayTests: [],
      selectRecruits: [],
      selectTests: [],
      recruitImg: [],
      recruitList: [],
    }
  },
  components: {
    RecruitModal
  },
  mounted() {
    // let today = new Date();   
    // let year = String(today.getFullYear()).substring(0,2);
    // let month = '0' + String(today.getMonth() + 1);
    // let date = String(today.getDate());
    // let custom_date = Number(year + month + date)
    // this.todatSchedule(custom_date)
    // this.getRecruitInform()
    this.getRecruit()
  },
  methods: {
    ...mapMutations(['setUserDivide', 'setRecruitId']),
    selectDate() {
      this.isSelect = true
      const Day = event.path[0].innerText
      if (Day.length == 1) {
        this.selectDay = '0' + Day
      } else {
        this.selectDay = Day
      }
      const Month = event.path[5].childNodes[0].childNodes[1].innerText.split(' ')[0].substring(0,3)
      this.setMonth(Month)
      this.selectYear = event.path[5].childNodes[0].childNodes[1].innerText.split(' ')[1]
      this.selectSchedule(Number(this.selectYear.substring(0,2)+this.selectMonth+this.selectDay))
    },
    setMonth(month) {
      if (month === 'Jan') {this.selectMonth = '01'} else if (month === 'Feb') {this.selectMonth = '02'}
      else if (month === 'Mar') {this.selectMonth = '03'} else if (month === 'Apr') {this.selectMonth = '04'}
      else if (month === 'May') {this.selectMonth = '05'} else if (month === 'Jun') {this.selectMonth = '06'}
      else if (month === 'Jul') {this.selectMonth = '07'} else if (month === 'Aug') {this.selectMonth = '08'}
      else if (month === 'Sep') {this.selectMonth = '09'} else if (month === 'Oct') {this.selectMonth = '10'}
      else if (month === 'Nov') {this.selectMonth = '11'} else {this.selectMonth = '12'}
    },
    selectSchedule(date) {
      // console.log(this.defaultSchedule[date])
      // console.log(this.defaultSchedule[date].recruit)
      // console.log(this.defaultSchedule[date].test)
      this.selectRecruits = this.defaultSchedule[date].recruit
      this.selectTests = this.defaultSchedule[date].test
    },
    todatSchedule(date) {
      this.todayRecruits = this.defaultSchedule[date].recruit
      this.todayTests = this.defaultSchedule[date].test
    },
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
        console.log(this.recruitList,'dsdsds')
        for(let i=0; i<res.data.length; i++) {
          axios.get(`${SERVER_URL}articles/${res.data[i].user.id}/`, null, config)
          .then(res => {
            this.recruitImg.push(res.data.image)
            console.log(this.recruitImg)
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