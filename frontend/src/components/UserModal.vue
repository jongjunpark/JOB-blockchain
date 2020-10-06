<template>
  <transition name="modal">
    <div class="user-modal-mask">
      <div @click.self="$emit('close')">
        <div class="user-modal-wrap">
          <div class="user-modal-content">
            <i class="fas fa-times" @click.self="$emit('close')"></i>
            <div class='user-modal-header'>
              <p class="user-modal-corp-name">네이버</p>
              <p class="user-modal-name"><span>경력</span>물류 경력사원 채용</p>
              <p class="user-modal-date">~ 2020.11.01 18:00</p>
            </div>
            <div class='user-modal-body'>
              <img src="#" alt="">
            </div>
            <div class="user-modal-footer">
              <div class="user-modal-btn">전체목록</div>
              <div class="user-modal-btn">저장목록</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex';
// import './css/user-modal.css'
// import axios from 'axios'

// const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'UserModal',
  data() {
    return {
      getData: [],
      getLicense: [],
      getLang: [],
      getCareer: [],
      certifiedSchool: [[],[],[],[],[]],
      certifiedEtc: [[],[]],
      isCareerText: [],
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['UserInfo', 'UserModalId']),
  },
  created() {
  },
  mounted() {
    setTimeout(() => {
      this.getResume()
    }, 1000);
  },
  methods: {
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.UserModalId}/`, null, config)
      .then(res => {
        console.log(res,'get resume')
        this.getData = res.data
        this.sortSchool()
        this.sortEtc()
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/certificates/`, null, config)
      .then(res => {
        console.log(res,'get license')
        this.getLicense = res.data
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/languages/`, null, config)
      .then(res => {
        console.log(res,'get lang')
        this.getLang = res.data
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.UserModalId}/careers/`, null, config)
      .then(res => {
        console.log(res,'get career')
        this.getCareer = res.data
        for(let i=0; i<res.data.length; i++) {
          this.isCareerText.push(false)
        }
      })
      .catch((err) => console.log(err.response))
    },
  },
  sortSchool() {
    if(this.getData.highschool_name) {
      let ARR = ['고등학교']
      ARR.push(this.getData.highschool_name); ARR.push(this.getData.highschool_classification); ARR.push(this.getData.highschool_location);
      ARR.push(this.getData.highschool_entrance_year); ARR.push(this.getData.highschool_graduation_year);
      this.certifiedSchool[0] = ARR
    }
    if(this.getData.college_name) {
      let ARR = ['전문대학']
      ARR.push(this.getData.college_name); ARR.push(this.getData.college_classification); ARR.push(this.getData.college_location);
      ARR.push(this.getData.college_entrance_year); ARR.push(this.getData.college_graduation_year); ARR.push(this.getData.college_major);
      if (this.getData.college_minor) { ARR.push(this.getData.college_minor) } else { ARR.push('X') } ARR.push(this.getData.college_grade); ARR.push(this.getData.college_total)
      this.certifiedSchool[1] = ARR
    }
    if(this.getData.university_name) {
      let ARR = ['대학교']
      ARR.push(this.getData.university_name); ARR.push(this.getData.university_classification); ARR.push(this.getData.university_location);
      ARR.push(this.getData.university_entrance_year); ARR.push(this.getData.university_graduation_year); ARR.push(this.getData.university_major);
      if (this.getData.university_minor) { ARR.push(this.getData.university_minor) } else { ARR.push('X') } ARR.push(this.getData.university_grade); ARR.push(this.getData.university_total)
      this.certifiedSchool[2] = ARR
    }
    if(this.getData.master_name) {
      let ARR = ['석사']
      ARR.push(this.getData.master_name); ARR.push(this.getData.master_classification); ARR.push(this.getData.master_location);
      ARR.push(this.getData.master_entrance_year); ARR.push(this.getData.master_graduation_year); ARR.push(this.getData.master_major);
      if (this.getData.master_minor) { ARR.push(this.getData.master_minor) } else { ARR.push('X') } ARR.push(this.getData.master_grade); ARR.push(this.getData.master_total)
      this.certifiedSchool[3] = ARR
    }
    if(this.getData.doctor_name) {
      let ARR = ['박사']
      ARR.push(this.getData.doctor_name); ARR.push(this.getData.doctor_classification); ARR.push(this.getData.doctor_location);
      ARR.push(this.getData.doctor_entrance_year); ARR.push(this.getData.doctor_graduation_year); ARR.push(this.getData.doctor_major);
      if (this.getData.doctor_minor) { ARR.push(this.getData.doctor_minor) } else { ARR.push('X') } ARR.push(this.getData.doctor_grade); ARR.push(this.getData.doctor_total)
      this.certifiedSchool[4] = ARR
    }
  },
  sortEtc() {
    if(this.getData.veterans_classification) {
      let ARR = ['보훈']
      ARR.push(this.getData.veterans_classification); ARR.push(this.getData.veterans_number);
      this.certifiedEtc[0] = ARR
    }
    if(this.getData.obstacle_classification) {
      let ARR = ['장애']
      ARR.push(this.getData.obstacle_classification); ARR.push(this.getData.obstacle_grade);
      this.certifiedEtc[1] = ARR
    }
  },
  onCareerText(text, idx) {
    if (text === 'on') {
      this.isCareerText[idx] = true
    } else {
      this.isCareerText[idx] = false
    }
  },
}
</script>

<style scoped>
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

}

.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

}

.user-modal-mask {
  position: fixed;
  z-index: 99999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
  overflow-x: hidden;
  overflow-y: auto;
}

.user-modal-mask > div {
  overflow: auto;
  height: 100%;
}

.user-modal-mask .fa-times {
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
  color: rgba(0,0,0,0.8);
  font-size: 25px;
  transition: all .3s;
}

.user-modal-mask .fa-times:hover {
  color: #0088ff;
}

.modal-enter .user-modal-wrap,
.modal-leave-active .user-modal-wrap {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.user-modal-wrap {
  /* position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%); */
  margin: 50px auto;
  transition: 0.3s ease;
  background-color: #eff0f5;
  border-radius: 1vw;
  width: 600px;
  /* margin-top: 50px;
  margin-bottom: 50px; */
}

.user-modal-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px 30px;
}


.user-modal-content .user-modal-header {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.user-modal-content .user-modal-header p:nth-child(1) {
  font-size: 25px;
  font-weight: 500;
  margin-bottom: 10px;
}

.user-modal-content .user-modal-header p:nth-child(2) {
  font-size: 30px;
  font-weight: 700;
  margin-bottom: 5px;
  display: flex;
  align-items: center;
}

.user-modal-header .user-modal-name > span {
  padding: 5px 10px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  font-size: 14px;
  margin-right: 10px;
  margin-top: 5px
}

.user-modal-content .user-modal-body {
  width: 100%;
  background-color: grey;
  margin: 20px 0;
}

.user-modal-content .user-modal-body > img {
  width: 100%;
  height: 800px;
}

.user-modal-footer {
  width: 100%;
  display: flex;
  justify-content: center;
  margin: 10px 0;
}

.user-modal-footer > div {
  margin: 0 50px;
  width: 30%;
  height: 50px;
  border-radius: 30px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  background-color: #0088ff;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  cursor: pointer;
  transition: box-shadow .3s;
}

.user-modal-footer > div:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  font-weight: 700;
}
</style>