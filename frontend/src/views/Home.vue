<template>
  <div class='wrap'>
    <div class="wrap-container home-container">
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
                  <div class="recruit-slide slide_1">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/samsung.png" alt="">
                          </div>
                          <p>삼성SDI</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/naver.png" alt="">
                          </div>
                          <p>네이버</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/kakao.png" alt="">
                          </div>
                          <p>카카오</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="recruit-slide slide_2">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/SK.png" alt="">
                          </div>
                          <p>SK그룹</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/LG.png" alt="">
                          </div>
                          <p>LG그룹</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/cj.png" alt="">
                          </div>
                          <p>CJ그룹</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="recruit-slide slide_3">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/doosan.png" alt="">
                          </div>
                          <p>두산그룹</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/hyundai.png" alt="">
                          </div>
                          <p>현대자동차</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/kia.png" alt="">
                          </div>
                          <p>기아자동차</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="recruit-slide slide_4">
                    <div class="recruit-slide-content">
                      <div class="recruit-card-box">
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/apm.png" alt="">
                          </div>
                          <p>Applied Materials</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/asml.png" alt="">
                          </div>
                          <p>ASML</p>
                        </div>
                        <div class="recruit-card">
                          <div class="recruit-card-img-box">
                            <img src="@/assets/images/gs.png" alt="">
                          </div>
                          <p>GS그룹</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          
        </div>
        <div class="test-box">
          <p class="test-header">다가오는 시험</p>
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
                  <div class="test-slide slide_1">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card">
                          <div class="test-card-countdown countdown-lastday">D - 1</div>
                          <div class="test-card-content">
                            <p class="test-card-head">2020 기사 제4회 실기시험</p>
                            <p class="test-card-footer">한국산업인력공단</p>
                          </div>
                        </div>
                        <div class="test-card">
                          <div class="test-card-countdown">D - 3</div>
                          <div class="test-card-content">
                            <p class="test-card-head">제49회 SQLD</p>
                            <p class="test-card-footer">한국데이터산업진흥원</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="test-slide slide_2">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card">
                          <div class="test-card-countdown">D - 6</div>
                          <div class="test-card-content">
                            <p class="test-card-head">2020 기사 제5회 필기시험</p>
                            <p class="test-card-footer">한국산업인력공단</p>
                          </div>
                        </div>
                        <div class="test-card">
                          <div class="test-card-countdown">D - 7</div>
                          <div class="test-card-content">
                            <p class="test-card-head">OPIC</p>
                            <p class="test-card-footer">ACTFL</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="test-slide slide_3">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card">
                          <div class="test-card-countdown">D - 11</div>
                          <div class="test-card-content">
                            <p class="test-card-head">제 129회 TOEIC</p>
                            <p class="test-card-footer">한국 토익 위원회</p>
                          </div>
                        </div>
                        <div class="test-card">
                          <div class="test-card-countdown">D - 14</div>
                          <div class="test-card-content">
                            <p class="test-card-head">제50회 SQLD</p>
                            <p class="test-card-footer">한국데이터산업진흥원</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="test-slide slide_4">
                    <div class="test-slide-content">
                      <div class="test-card-box">
                        <div class="test-card">
                          <div class="test-card-countdown">D - 17</div>
                          <div class="test-card-content">
                            <p class="test-card-head">2020 기능사 제4회 필기시험</p>
                            <p class="test-card-footer">한국산업인력공단</p>
                          </div>
                        </div>
                        <div class="test-card">
                          <div class="test-card-countdown">D - 20</div>
                          <div class="test-card-content">
                            <p class="test-card-head">제215회 워드프로세서</p>
                            <p class="test-card-footer">대한상공회의소</p>
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
      <div class="calendar-box">
        <p class="calendar-header">일정</p>
        <div class="calendar">
          <SingleDatePicker class='test' @selectDate='selectDate'/>
          <div class="calendar-content">
            <div v-if="!isSelect">
              <span>오늘의 일정</span>
              <div class='calendar-select-box'>
                <div v-for="recruit in todayRecruits" :key="recruit" class='calendar-recruit-box'>
                  <div class='calendar-select-type'>채용</div>
                  {{ recruit }}
                </div>
                <div v-for="test in todayTests" :key="test" class='calendar-test-box'>
                  <div class='calendar-select-type'>시험</div>
                  {{ test }}
                </div>
              </div>
            </div>
            <div v-if='isSelect'>
              <span>{{ selectYear.substring(0,2) }}.</span>
              <span>{{ selectMonth }}.</span>
              <span>{{ selectDay }} 일정 </span>
              <div class='calendar-select-box'>
                <div v-for="recruit in selectRecruits" :key="recruit" class='calendar-recruit-box'>
                  <div class='calendar-select-type'>채용</div>
                  {{ recruit }}
                </div>
                <div v-for="test in selectTests" :key="test" class='calendar-test-box'>
                  <div class='calendar-select-type'>시험</div>
                  {{ test }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import SingleDatePicker from 'vue-single-date-picker';
import 'vue-single-date-picker/dist/vue-single-date-picker.css';
import '../components/css/home.css'

// const WORK_API_KEY = process.env.VUE_APP_WORK_API_KEY

export default {
  name: 'Home',
  data() {
    return {
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
        200919 : {
          recruit: ['삼성전자', '카카오'],
          test: ['기사 제4회 실기시험'],
        },
      },
      todayRecruits: [],
      todayTests: [],
      selectRecruits: [],
      selectTests: [],
    }
  },
  components: {
    SingleDatePicker
  },
  mounted() {
    let today = new Date();   
    let year = String(today.getFullYear()).substring(0,2);
    let month = '0' + String(today.getMonth() + 1);
    let date = String(today.getDate());
    let custom_date = Number(year + month + date)
    this.todatSchedule(custom_date)
    // this.getRecruitInform()
  },
  methods: {
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