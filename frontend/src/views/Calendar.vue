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
        <p>오늘의 일정</p>
        <div class="calendar-recruit-inner-box">
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
          <div class="calendar-recruit-card"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SingleDatePicker from 'vue-single-date-picker';
import 'vue-single-date-picker/dist/vue-single-date-picker.css';

export default {
  name: 'Calendar',
  data() {
    return {
      test: '',
    }
  },
  components: {
    SingleDatePicker,
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
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
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
  margin-top: 20px;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  overflow: auto;
  max-height: 400px;
}

.calendar-recruit-inner-box .calendar-recruit-card {
  width: calc(50% - 20px);
  height: 60px;
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
</style>