<template>
  <div class="wrap resume-wrap">
    <div class="wrap-container resume-container">
      <div class="resume-user-box">
        <div class="resume-user-content">
          <img v-if="!getData.image" src="@/assets/images/default-user.png" alt="#">
          <img v-if="getData.image" :src="'http://localhost:8000' + getData.image" alt="#">
          <p class="resume-user-name">{{ getData.name }}</p>
          <p class="resume-user-birth">{{ getData.date_of_birth }}</p>
          <p class="resume-user-email">{{ getData.email }}</p>
          <p class="resume-user-number">{{ getData.phone_number }}</p>
          <div class="resume-user-btn" @click="goResumeEdit" v-if="!isBuy">구매하기</div>
        </div>
      </div>
      <div class="resume-data-box resume-modal-unlock">
        <div class="resume-data-content-box">
          <p>병역사항</p>
          <div class="resume-data-content">
            <p v-if="!getData.military_classification">인증된 병력사항이 없습니다.</p>
            <div v-if="getData.military_classification" class="resume-license-certified-list">
              <div class="resume-detail resume-type">{{ getData.military_classification }}</div>
              <div class="resume-detail">{{ getData.military_branch }}</div>
              <div class="resume-detail">{{ getData.military_rank }}</div>
              <div class="resume-detail">{{ getData.military_completed }}</div>
              <div v-if="getData.military_completed_reason" class="resume-detail">{{ getData.military_completed_reason }}</div>
              <div class="resume-detail resume-detail-non-margin">{{ getData.military_start }}</div>
              <div class="resume-detail resume-detail-non-margin">~</div>
              <div class="resume-detail">{{ getData.military_end }}</div>
              <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>학력사항</p>
          <div class="resume-data-content">
            <p v-if="(certifiedSchool[0].length+certifiedSchool[1].length+certifiedSchool[2].length
            +certifiedSchool[3].length+certifiedSchool[4].length)===0">인증된 학력사항이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(certified, index) in certifiedSchool' :key='`certified-${index}`'>
              <div class="resume-license-certified-list" v-if="certified[0]">
                <div class="resume-detail resume-type">{{ certified[0] }}</div>
                <div class="resume-detail">{{ certified[1] }}</div><div class="resume-detail">{{ certified[2] }}</div>
                <div class="resume-detail">{{ certified[3] }}</div><div class="resume-detail resume-detail-non-margin">{{ certified[4] }}</div>
                <div class="resume-detail resume-detail-non-margin">~</div><div class="resume-detail">{{ certified[5] }}</div>
                <div v-if="certified[6]" class="resume-detail resume-detail-non-margin">{{ certified[6] }}</div>
                <div v-if="certified[6]" class="resume-detail resume-detail-non-margin">/</div>
                <div v-if="certified[7]" class="resume-detail">{{ certified[7] }}</div>
                <div v-if="certified[8]" class="resume-detail resume-detail-non-margin">{{ certified[8] }}</div>
                <div v-if="certified[8]" class="resume-detail resume-detail-non-margin">/</div><div v-if="certified[9]" class="resume-detail">{{ certified[9] }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>자격사항</p>
          <div class="resume-data-content">
            <p v-if="getLicense.length===0">인증된 자격증이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(license, index) in getLicense' :key='`license1-${index}`'>
              <div class="resume-license-certified-list" v-if="license.name">
                <div class="resume-detail resume-type">{{ license.name }}</div>
                <div class="resume-detail">{{ license.publisher }}</div><div class="resume-detail">{{ license.date }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>어학사항</p>
          <div class="resume-data-content">
            <p v-if="getLang.length===0">인증된 어학성적이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(lang, index) in getLang' :key='`lang1-${index}`'>
              <div class="resume-license-certified-list" v-if="lang.classification">
                <div class="resume-detail resume-type">{{ lang.classification }}</div>
                <div class="resume-detail">{{ lang.name }}</div><div class="resume-detail">{{ lang.score }}</div>
                <div class="resume-detail">{{ lang.date }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>경력사항</p>
          <div class="resume-data-content">
            <p v-if="getCareer.length===0">인증된 경력이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(career, index1) in getCareer' :key='`career1-${index1}`'>
              <div class="resume-license-certified-list" v-if="career.name">
                <div class="resume-detail resume-type">{{ career.name }}</div>
                <div class="resume-detail resume-detail-non-margin">{{ career.start_term }}</div>
                <div class="resume-detail resume-detail-non-margin">~</div>
                <div class="resume-detail">{{ career.end_term }}</div>
                <div class="resume-detail">{{ career.retirement_reason }}</div><div class="resume-detail">{{ career.department }}</div>
                <div class="resume-detail">{{ career.rank }}</div><div class="resume-detail">{{ career.duty }}</div>
                <div class="resume-detail resume-detail-career-text" @mouseenter="onCareerText1('on', index1)" @mouseleave="onCareerText1('off', index1)">
                  경력기술서
                  <div v-if="isCareerText[index1]">{{ career.statement }}</div>
                </div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>기타</p>
          <div class="resume-data-content">
            <p v-if="(certifiedEtc[0].length+certifiedEtc[1].length)===0">인증된 기타사항이 없습니다.</p>
            <div class="resume-license-resume-list" v-for='(etc, index) in certifiedEtc' :key='`etc-${index}`'>
              <div class="resume-license-certified-list" v-if="(etc[0] || etc[1])">
                <div class="resume-detail resume-type">{{ etc[0] }}</div>
                <div class="resume-detail">{{ etc[1] }}</div><div class="resume-detail">{{ etc[2] }}</div>
                <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ResumeBuy :id="id" v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';
import ResumeBuy from '../components/BuyResume.vue';

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'Resume',
  data() {
    return {
      id: 0,
      getData: [],
      getLicense: [],
      getLang: [],
      getCareer: [],
      certifiedSchool: [[],[],[],[],[]],
      certifiedEtc: [[],[]],
      isCareerText: [],
      showModal: false,
      isBuy: false,
    }
  },
  components: {
    ResumeBuy
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    setTimeout(() => {
      this.getResume()
    }, 1000);
    this.id = this.$route.params.id
    console.log(this.id)
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}accounts/item/list/${this.id}/`, null, config)
      .then(res => {
        if (res.data.result == 1) {
          this.isBuy = true
          const Lock = document.querySelector('.resume-modal-unlock')
          Lock.classList.remove('resume-modal-unlock')
        }
        else {
          this.isBuy = false
        }
      })
      .catch((err) => console.log(err.response))
  },
  watch: {
    showModal() {
      this.id = this.$route.params.id
      console.log(this.id)
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.post(`${SERVER_URL}accounts/item/list/${this.id}/`, null, config)
        .then(res => {
          if (res.data.result == 1) {
            this.isBuy = true
            const Lock = document.querySelector('.resume-modal-unlock')
          Lock.classList.remove('resume-modal-unlock')
          }
          else {
            this.isBuy = false
          }
        })
        .catch((err) => console.log(err.response))
    },
  },
  methods: {
    goResumeEdit() {
      this.showModal = true
    },
    handleScroll() {
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.resume-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    onCareerText(text, idx) {
      if (text === 'on') {
        this.isCareerText[idx] = true
      } else {
        this.isCareerText[idx] = false
      }
    },
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.id}/`, null, config)
      .then(res => {
        console.log(res,'get resume')
        this.getData = res.data
        this.sortSchool()
        this.sortEtc()
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.id}/certificates/`, null, config)
      .then(res => {
        console.log(res,'get license')
        this.getLicense = res.data
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.id}/languages/`, null, config)
      .then(res => {
        console.log(res,'get lang')
        this.getLang = res.data
      })
      .catch((err) => console.log(err.response))

      axios.get(`${SERVER_URL}articles/${this.id}/careers/`, null, config)
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
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>
.resume-wrap {
  padding: 0 100px !important;
  width: 1000px !important;
}

.resume-container {
  flex-direction: row;
}

.resume-container .resume-user-box {
  width: 22%;
  height: 30px;
  position: relative;
  /* background-color: hotpink; */
}

.resume-user-box .resume-user-content {
  width: calc(90% - 40px);
  /* background-color: indigo; */
  position: absolute;
  padding: 30px;
  top:0;
  left:50%;
  transform: translate(-50%, 0);
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
}

.resume-user-content > img {
  width: 100%;
  height: 200px;
  border-radius: 15px;
}

.resume-user-content > p {
  margin: 5px 0;
  font-size: 12px;
}

.resume-user-content > p:nth-child(2) {
  font-size: 20px;
  font-weight: 700;
}

.resume-user-content .resume-user-btn {
  width: 100%;
  height: 40px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  margin-top: 20px;
  background-color: #0088ff;
  color: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: box-shadow .3s;
}

.resume-user-content .resume-user-btn:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  font-weight: 700;
}

.resume-container .resume-data-box {
  width: 80%;
  height: 30px;
  /* background-color: greenyellow; */
}

.resume-data-box .resume-data-content-box {
  width: calc(100% - 100px);
  margin: 30px 0 30px 20px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  padding: 20px 30px 30px 30px;
}

.resume-data-content-box > p {
  font-family: 'TmonMonsori';
  margin-bottom: 20px;
  font-weight: 500;
  font-size: 25px;
}

.resume-data-box .resume-data-content {
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

.resume-data-box .resume-data-content > p {
  font-size: 11px;
  margin: 10px 0;
}

.resume-data-content .resume-license-certified-list {
  width: 100%;
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.resume-data-content .resume-license-resume-list {
  width: 100%;
  display: flex;
  align-items: center;
}

.resume-license-certified-list .resume-detail {
  margin-right: 15px;
  font-size: 11px;
}

.resume-license-certified-list .resume-detail-non-margin {
  margin-right: 5px;
}

.resume-license-certified-list .resume-detail-career-text {
  color: #0088ff;
  position: relative;
  cursor: pointer;
}

.resume-license-certified-list .resume-type {
  margin-right: 15px;
  padding: 5px 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
}

.resume-detail-career-text > div {
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

.resume-license-certified-list .resume-mark-box {
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

.resume-mark-box .fa-check-circle {
  margin-right: 5px;
}

.resume-modal-unlock {
  filter: blur(3px);
}

</style>