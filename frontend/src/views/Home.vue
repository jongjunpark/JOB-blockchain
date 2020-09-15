<template>
  <div class='wrap'>
    <div class="wrap-container home-container">
      <div class="schedule-box">
        <div class="recruit-box">
          <p class="recruit-header">추천공고</p>
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
        <div class="test-box">
          <p class="test-header">다가오는 시험</p>
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
import SingleDatePicker from 'vue-single-date-picker';
import 'vue-single-date-picker/dist/vue-single-date-picker.css';

export default {
  name: 'Home',
  data() {
    return {
      selectYear: '',
      selectMonth: '',
      selectDay: '',
      isSelect: false,
      defaultSchedule: {
        200915 : {
          recruit: ['네이버', '삼성전자', '카카오'],
          test: ['제49회 SQLD', '기사 제4회 실기시험'],
        },
        200916 : {
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
    }
  }
}
</script>

<style>
#single-date-picker {
  width: 100% !important;
}

.home-container {
  flex-direction: row;
}

.home-container .schedule-box {
}

.home-container .calendar-box {
  display: flex;
  flex-direction: column;
  margin-left: 50px;
}

.schedule-box .recruit-box {
  display: flex;
  flex-direction: column;
}

.recruit-box .recruit-header {
  margin: 40px 0 15px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.recruit-box .recruit-card-box {
  display: flex;
  justify-content: space-between;
}

.recruit-card-box .recruit-card {
  width: 220px;
  height: 250px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  border: 1px solid rgba(0,0,0,0);
  margin-right: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.recruit-card-box .recruit-card .recruit-card-img-box {
  display: flex;
  height: 60%;
  width: 70%;
  margin-top: 10px;
  justify-content: center;
  align-items: center;
}

.recruit-card-box .recruit-card img {
  width: 70%;
}

.recruit-card-box .recruit-card p {
  font-size: 18px;
  font-weight: 700;
  margin-top: 10px;
  color: rgba(0,0,0,0.7);
}

.schedule-box .test-box {
  display: flex;
  flex-direction: column;
}

.test-box .test-header {
  margin: 40px 0 15px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.test-box .test-card-box {
  display: flex;
  justify-content: space-between;
}

.test-card-box .test-card {
  min-width: 340px;
  height: 180px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  border: 1px solid rgba(0,0,0,0);
  margin-right: 20px;
  display: flex;
  flex-direction: column;
}

.test-card .test-card-countdown {
  width: 80px;
  height: 50px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border-radius: 20px;
  margin: 15px 0 0 15px;
  font-weight: 900;
  display: flex;
  justify-content: center;
  align-items: center;
}

.test-card .countdown-lastday {
  color: red;
}

.test-card .test-card-content {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  width: 100%;
  height: 100%;
  padding-bottom: 10px;
}

.test-card-content .test-card-head {
  font-size: 18px;
  font-weight: 700;
  color: rgba(0,0,0,0.7)
}

.test-card-content .test-card-footer {
  font-size: 15px;
  color: rgba(0,0,0,0.7)
}

.calendar-box .calendar-header {
  margin: 40px 0 15px 10px;
  font-size: 20px;
  font-weight: 900;
  color: #0088ff;
}

.calendar-box .calendar {
  width: 500px;
  height: 520px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
}

.calendar-box .calendar-content {
  display: flex;
  margin-left: 30px;
  color: rgba(0,0,0,0.7);
  font-weight: 700;
}

.calendar-content .calendar-select-box {
  margin-top: 10px;
}

.calendar-select-box .calendar-recruit-box {
  display: flex;
  margin-bottom: 10px;
  align-items: center;
  font-size: 15px;
}

.calendar-select-box .calendar-test-box {
  display: flex;
  margin-bottom: 10px;
  align-items: center;
  font-size: 15px;
}

.calendar-select-box .calendar-select-type {
  background-color: aquamarine;
  width: 40px;
  height: 25px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 20px;
}

.calendar-test-box .calendar-select-type {
  background-color: rgb(255, 246, 167);
}

.calendar-recruit-box > div, .calendar-test-box > div {
  font-size: 13px;
}

.calendar-content span {
  font-weight: 900;
}

</style>