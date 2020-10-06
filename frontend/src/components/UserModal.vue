<template>
  <transition name="modal">
    <div class="user-modal-mask">
      <div @click.self="$emit('close')">
        <div class="user-modal-wrap">
          <div class="user-modal-content">
            <i class="fas fa-times" @click.self="$emit('close')"></i>
            <div class='user-modal-header'>
              <div class="user-modal-img-box">
                <img v-if="getData.image" :src="getData.image" alt="#">
                <img v-if="!getData.image" src="@/assets/images/default-user.png" alt="#">
              </div>
              <div class="user-modal-text-box">
                <p>{{ getData.name }}</p>
                <p>{{ getData.date_of_birth }}</p>
                <p>{{ getData.email }}</p>
                <p>{{ getData.phone_number }}</p>
              </div>
            </div>
            <div class='user-modal-body'>
              <div class="user-modal-content-box">
                <p>병역사항</p>
                <div class="user-modal-data-content">
                  <p v-if="!getData.military_classification">인증된 병력사항이 없습니다.</p>
                  <div v-if="getData.military_classification" class="user-modal-license-certified-list">
                    <div class="user-modal-detail user-modal-type">{{ getData.military_classification }}</div>
                    <div class="user-modal-detail">{{ getData.military_branch }}</div>
                    <div class="user-modal-detail">{{ getData.military_rank }}</div>
                    <div class="user-modal-detail">{{ getData.military_completed }}</div>
                    <div v-if="getData.military_completed_reason" class="user-modal-detail">{{ getData.military_completed_reason }}</div>
                    <div class="user-modal-detail user-modal-detail-non-margin">{{ getData.military_start }}</div>
                    <div class="user-modal-detail user-modal-detail-non-margin">~</div>
                    <div class="user-modal-detail">{{ getData.military_end }}</div>
                    <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>학력사항</p>
                <div class="user-modal-data-content">
                  <p v-if="(certifiedSchool[0].length+certifiedSchool[1].length+certifiedSchool[2].length
                  +certifiedSchool[3].length+certifiedSchool[4].length)===0">인증된 학력사항이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(certified, index) in certifiedSchool' :key='`certified-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="certified[0]">
                      <div class="user-modal-detail user-modal-type">{{ certified[0] }}</div>
                      <div class="user-modal-detail">{{ certified[1] }}</div><div class="user-modal-detail">{{ certified[2] }}</div>
                      <div class="user-modal-detail">{{ certified[3] }}</div><div class="user-modal-detail user-modal-detail-non-margin">{{ certified[4] }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">~</div><div class="user-modal-detail">{{ certified[5] }}</div>
                      <div v-if="certified[6]" class="user-modal-detail user-modal-detail-non-margin">{{ certified[6] }}</div>
                      <div v-if="certified[6]" class="user-modal-detail user-modal-detail-non-margin">/</div>
                      <div v-if="certified[7]" class="user-modal-detail">{{ certified[7] }}</div>
                      <div v-if="certified[8]" class="user-modal-detail user-modal-detail-non-margin">{{ certified[8] }}</div>
                      <div v-if="certified[8]" class="user-modal-detail user-modal-detail-non-margin">/</div><div v-if="certified[9]" class="user-modal-detail">{{ certified[9] }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>자격사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getLicense.length===0">인증된 자격증이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(license, index) in getLicense' :key='`license1-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="license.name">
                      <div class="user-modal-detail user-modal-type">{{ license.name }}</div>
                      <div class="user-modal-detail">{{ license.publisher }}</div><div class="user-modal-detail">{{ license.date }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>어학사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getLang.length===0">인증된 어학성적이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(lang, index) in getLang' :key='`lang1-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="lang.classification">
                      <div class="user-modal-detail user-modal-type">{{ lang.classification }}</div>
                      <div class="user-modal-detail">{{ lang.name }}</div><div class="user-modal-detail">{{ lang.score }}</div>
                      <div class="user-modal-detail">{{ lang.date }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>경력사항</p>
                <div class="user-modal-data-content">
                  <p v-if="getCareer.length===0">인증된 경력이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(career, index1) in getCareer' :key='`career1-${index1}`'>
                    <div class="user-modal-license-certified-list" v-if="career.name">
                      <div class="user-modal-detail user-modal-type">{{ career.name }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">{{ career.start_term }}</div>
                      <div class="user-modal-detail user-modal-detail-non-margin">~</div>
                      <div class="user-modal-detail">{{ career.end_term }}</div>
                      <div class="user-modal-detail">{{ career.retirement_reason }}</div><div class="user-modal-detail">{{ career.department }}</div>
                      <div class="user-modal-detail">{{ career.rank }}</div><div class="user-modal-detail">{{ career.duty }}</div>
                      <div class="user-modal-detail user-modal-detail-career-text" @mouseenter="onCareerText('on', index1)" @mouseleave="onCareerText('off', index1)">
                        경력기술서
                        <div v-if="isCareerText[index1]">{{ career.statement }}</div>
                      </div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="user-modal-content-box">
                <p>기타</p>
                <div class="user-modal-data-content">
                  <p v-if="(certifiedEtc[0].length+certifiedEtc[1].length)===0">인증된 기타사항이 없습니다.</p>
                  <div class="user-modal-license-user-modal-list" v-for='(etc, index) in certifiedEtc' :key='`etc-${index}`'>
                    <div class="user-modal-license-certified-list" v-if="(etc[0] || etc[1])">
                      <div class="user-modal-detail user-modal-type">{{ etc[0] }}</div>
                      <div class="user-modal-detail">{{ etc[1] }}</div><div class="user-modal-detail">{{ etc[2] }}</div>
                      <div class="user-modal-detail user-modal-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="user-modal-footer">
              <div class="user-modal-btn" @click.self="$emit('close')">닫기</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex';
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

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
        if(this.getData.image) {
          this.getData.image = 'http://localhost:8000' + this.getData.image
        }
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
  top: 25px;
  right: 25px;
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
  border-radius: 20px;
  width: 800px;
  /* margin-top: 50px;
  margin-bottom: 50px; */
}

.user-modal-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 70px 80px;
  padding-bottom: 30px;
  position: relative;
}


.user-modal-content .user-modal-header {
  width: 100%;
  display: flex;
}

.user-modal-header .user-modal-img-box {
  width: 25%;
  height: 200px;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  border-radius: 20px;
  margin-right: 40px;
}

.user-modal-header .user-modal-img-box > img {
  width: 100%;
  height: 100%;
  border-radius: 15px;
}

.user-modal-header .user-modal-text-box p {
  font-size: 14px;
  margin-bottom: 20px;
  margin-top: 20px;
}

.user-modal-header .user-modal-text-box p:nth-child(1) {
  font-size: 25px !important;
  font-weight: 700;
}

.user-modal-content .user-modal-body {
  width: 100%;
  margin-top: 40px;
}

.user-modal-body .user-modal-content-box {
  margin-bottom: 50px;
}

.user-modal-body .user-modal-content-box > p {
  font-size: 25px;
  font-weight: 700;
  font-family: 'TmonMonsori';
  margin-bottom: 10px;
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

.user-modal-content-box .user-modal-data-content {
  width: 94%;
  margin-left: calc(6% - 35px);
  padding: 10px 15px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.user-modal-content-box .user-modal-data-content > p {
  font-size: 11px;
  margin: 10px 0;
}

.user-modal-data-content .user-modal-license-certified-list {
  width: 100%;
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.user-modal-data-content .user-modal-license-user-modal-list {
  width: 100%;
  display: flex;
  align-items: center;
}

.user-modal-license-certified-list .user-modal-detail {
  margin-right: 15px;
  font-size: 11px;
}

.user-modal-license-certified-list .user-modal-detail-non-margin {
  margin-right: 5px;
}

.user-modal-license-certified-list .user-modal-detail-career-text {
  color: #0088ff;
  position: relative;
  cursor: pointer;
}

.user-modal-license-certified-list .user-modal-type {
  margin-right: 15px;
  padding: 5px 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
}

.user-modal-detail-career-text > div {
  position: absolute;
  top: 100%;
  left: 0;
  width: 300px;
  padding: 10px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  cursor: auto;
  color: rgba(0,0,0,0.7);
  z-index: 100;
}

.user-modal-license-certified-list .user-modal-mark-box {
  padding: 5px 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0088ff;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  color: #ffffff;
}

.user-modal-mark-box .fa-check-circle {
  margin-right: 5px;
}
</style>