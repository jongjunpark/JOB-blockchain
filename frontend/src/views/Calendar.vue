<template>
  <div class="wrap">
    <div class="wrap-container calendar-container">
      <div class="calendar-box">
        <div class="calendar-header"></div>
        <div class="calendar">
          <SingleDatePicker class='test' @selectDate='selectDate'/>
          <!-- <div class="calendar-content"> -->
            <!-- <div v-if="!isSelect">
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
            </div> -->
            <!-- <div v-if='isSelect'>
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
            </div> -->
          <!-- </div> -->
        </div>
      </div>

      <div class="calendar-recruit-box">
        <p v-if="!isSelect">오늘의 일정</p>
        <p v-if="isSelect">{{selectYear.substring(0,2)}}.{{selectMonth}}.{{selectDay}}의 일정</p>
        <transition-group v-show="selectData" name='fade' tag="div" class="calendar-recruit-inner-box" mode="in-out">
          <div class="calendar-recruit-card" v-for='data in selectData' :key='data.id' @click="onModal(data.id)">
            <div>
              <p>{{ data.user.last_name }}</p>
              <p>~ {{data.deadline.substring(0,4)}}.{{data.deadline.substring(4,6)}}.{{data.deadline.substring(6,8)}}
                 {{data.deadline.substring(8,10)}}:{{data.deadline.substring(10,)}}
              </p>
            </div>
            <p><span>{{ data.division }}</span>{{ data.title }}</p>
          </div>
        </transition-group>
      </div>
    </div>

    <RecruitModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios'
import { mapMutations } from 'vuex';
import SingleDatePicker from 'vue-single-date-picker';
import RecruitModal from '../components/RecruitModal.vue'
import 'vue-single-date-picker/dist/vue-single-date-picker.css';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'Calendar',
  data() {
    return {
      showModal: false,
      isSelect: false,
      selectYear: '',
      selectMonth: '',
      selectDay: '',
      selectData: [],
      date: '',
    }
  },
  components: {
    SingleDatePicker,
    RecruitModal
  },
  computed: {
  },
  created() {
  },
  mounted() {
    let today = new Date();   
    let year = String(today.getFullYear());
    let month = String(today.getMonth() + 1);
    let date = String(today.getDate());
    if (month.length == 1) {
      month = '0' + month
    }
    if (date.length == 1) {
      date = '0' + date
    }
    let custom_date = Number(year + month + date)
    this.selectSchedule(Number(custom_date+'1200'))
  },
  watch: {
  },
  methods: {
    ...mapMutations(['setRecruitId']),
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
      this.selectSchedule(Number(this.selectYear+this.selectMonth+this.selectDay+'1200'))
      this.date = Number(this.selectYear.substring(0,2)+this.selectMonth+this.selectDay)
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
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}recruitments/calendar/${date}/`, null, config)
      .then(res => {
        console.log(res)
        this.selectData = res.data
      })
      .catch((err) => console.log(err.response))
      // console.log(this.defaultSchedule[date])
      // console.log(this.defaultSchedule[date].recruit)
      // console.log(this.defaultSchedule[date].test)
      // this.selectRecruits = this.defaultSchedule[date].recruit
      // this.selectTests = this.defaultSchedule[date].test
    },
    onModal(id) {
      this.setRecruitId(id)
      this.showModal = true;
    }
  },
}
</script>

<style>
.calendar-container {
  flex-direction: row !important;
}

.calendar-container .calendar-box {
 width: 40%; 
}

.calendar-box .calendar-header {
  font-family: 'TmonMonsori';
  margin: 60px 0 15px 10px;
  font-size: 20px;
  font-weight: 500;
  color: #0088ff;
}

.calendar-box .calendar {
  width: 500px;
  height: 530px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
}


.calendar-container .calendar-recruit-box {
  width: 60%;
  height: 530px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  margin-top: 60px;
  padding: 30px 20px;
  box-sizing: border-box;
}

.calendar-container .calendar-recruit-box > p {
  font-size: 25px;
  font-family: 'TmonMonsori';
  margin-left: 10px;
}

.calendar-recruit-box .calendar-recruit-inner-box {
  width: 100%;
  /* background-color: aqua; */
  margin-top: 10px;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  overflow: auto;
  max-height: 400px;
}

.calendar-recruit-inner-box .calendar-recruit-card {
  width: calc(50% - 55px);
  height: 50px;
  padding: 10px 15px;
  margin: 10px 10px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  transition: .5s;
  cursor: pointer;
}

.calendar-recruit-inner-box .calendar-recruit-card:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  background-color: #ececf0;
}

.calendar-recruit-card > div {
  display: flex;
  justify-content: space-between;
}

.calendar-recruit-card > div > p {
  font-size: 12px;
  font-weight: 500;
  margin-left: 5px;
}

.calendar-recruit-card > div > p:nth-child(2) {
  font-size: 10px;
  font-weight: 500;
  color: rgba(0,0,0,0.5);
}

.calendar-recruit-card > p {
  margin-top: 5px;
  font-size: 15px;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.calendar-recruit-card > p > span {
  margin-right: 10px;
  font-size: 10px;
  font-weight: 500;
  padding: 5px 8px;
  border-radius: 20px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
}


</style>