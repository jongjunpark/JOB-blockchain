<template>
  <div class="wrap resume-wrap">
    <div class="wrap-container resume-container">
      <div class="resume-user-box">
        <div class="resume-user-content">
          <img src="@/assets/images/default-user.png" alt="#">
          <p class="resume-user-name">박종준</p>
          <p class="resume-user-birth">1991. 05. 24</p>
          <p class="resume-user-email">poiufgin7373@naver.com</p>
          <p class="resume-user-number">010-5002-1524</p>
          <div class="resume-user-btn" @click="goResumeEdit">수정하기</div>
        </div>
      </div>
      <div class="resume-data-box">
        <div class="resume-data-content-box">
          <p>병역사항</p>
          <div class="resume-data-content">
            <p>인증된 병력사항이 없습니다.</p>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>학력사항</p>
          <div class="resume-data-content">
            <p>인증된 학력사항이 없습니다.</p>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>자격사항</p>
          <div class="resume-data-content">
            <p>인증된 자격사항이 없습니다.</p>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>어학사항</p>
          <div class="resume-data-content">
            <p>인증된 어학사항이 없습니다.</p>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>경력사항</p>
          <div class="resume-data-content">
            <p v-if="resumeCareer.length===0">인증된 경력사항이 없습니다.</p>
            <div class="resume-edit-license-resume-list" v-for='(career, index) in resumeCareer' :key='`career-${index}`'>
              <div class="resume-detail resume-type">{{ career[0] }}</div>
              <div class="resume-detail resume-detail-non-margin">{{ career[1] }}</div>
              <div class="resume-detail resume-detail-non-margin">~</div>
              <div class="resume-detail">{{ career[2] }}</div>
              <div class="resume-detail">{{ career[3] }}</div><div class="resume-detail">{{ career[4] }}</div>
              <div class="resume-detail">{{ career[5] }}</div><div class="resume-detail">{{ career[6] }}</div>
              <div class="resume-detail resume-detail-career-text" @mouseenter="onCareerText('on')" @mouseleave="onCareerText('off')">
                경력기술서
                <div v-if="isCareerText">{{ career[7] }}</div>
              </div>
              <div class="resume-detail resume-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
            </div>
          </div>
        </div>
        <div class="resume-data-content-box">
          <p>기타</p>
          <div class="resume-data-content">
            <p>인증된 기타사항이 없습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resume',
  data() {
    return {
      resumeCareer: [['삼성전자', '2020.01', '2020.07', '이직', '무선사업부', '책임', 'CS', '아무것도 안함']],
      isCareerText: false,
    }
  },
  components: {
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
    goResumeEdit() {
      this.$router.push('/resume/edit').catch(()=>{})
    },
    handleScroll() {
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.resume-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    onCareerText(text) {
      if (text === 'on') {
        this.isCareerText = true
      } else {
        this.isCareerText = false
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
  width: 25%;
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
  width: 75%;
  height: 30px;
  /* background-color: greenyellow; */
}

.resume-data-box .resume-data-content-box {
  width: calc(100% - 100px);
  margin: 30px 0 30px 20px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  padding: 20px 40px 30px 40px;
}

.resume-data-content-box > p {
  font-family: 'TmonMonsori';
  margin-bottom: 20px;
  font-weight: 500;
  font-size: 25px;
}

.resume-data-box .resume-data-content {
  width: 90%;
  margin-left: calc(5% - 20px);
  padding: 20px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.resume-data-box .resume-data-content > p {
  font-size: 13px;
}

.resume-data-content .resume-edit-license-resume-list {
  width: 100%;
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.resume-edit-license-resume-list .resume-detail {
  margin-right: 20px;
  font-size: 13px;
}

.resume-edit-license-resume-list .resume-detail-non-margin {
  margin-right: 5px;
}

.resume-edit-license-resume-list .resume-detail-career-text {
  color: #0088ff;
  position: relative;
  cursor: pointer;
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

.resume-edit-license-resume-list .resume-mark-box {
  width: 80px;
  height: 30px;
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
</style>