<template>
  <div class="wrap apply-wrap">
    <div class="wrap-container apply-container">
      <div class="apply-header">
        <div class="apply-header-text-box">
          <span>물류 경력사원 채용 </span>
          <span>(1800 명)</span>
        </div>
        <div class="apply-header-toggle-box">
          <div @click='applyInfoChange(false)' class="all-apply-btn apply-toggle-btn on-apply-btn">전체</div>
          <div @click='applyInfoChange(true)' class="some-apply-btn apply-toggle-btn">저장</div>
        </div>
      </div>
      <div class="apply-body">
        <div class="applicant-card">
          <div class="applicant-img-box">
            <img src="@/assets/images/default-user.png" alt="#">
          </div>
          <div class="applicant-text-box">
            <p>박종준</p>
            <p>1991. 05. 24</p>
            <p>poiufgin7373@naver.com</p>
            <p>010-5002-1524</p>
          </div>
        </div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
        <div class="applicant-card"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Base',
  data() {
    return {
      test: '',
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
    handleScroll() {
      console.log('Base')
    },
    applyInfoChange(bool) {
      const ALLBTN = document.querySelector('.all-apply-btn')
      const SOMEBTN = document.querySelector('.some-apply-btn')
      if (bool) {
        SOMEBTN.classList.add('on-apply-btn')
        ALLBTN.classList.remove('on-apply-btn')
      } else {
        ALLBTN.classList.add('on-apply-btn')
        SOMEBTN.classList.remove('on-apply-btn')
      }
    },
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>
.apply-wrap {
  padding: 0 100px !important;
  width: 1000px !important;
}

.apply-container {
  position: relative;
}

.apply-container .apply-header {
  margin-top: 50px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.apply-header .apply-header-text-box {
  display: flex;
  align-items: center;
}

.apply-header .apply-header-text-box > span:nth-child(1) {
  font-size: 20px;
  font-weight: 700;
  margin-right: 10px;
}

.apply-header .apply-header-text-box > span:nth-child(2) {
  font-size: 15px;
}

.apply-header-toggle-box {
  display: flex;
}

.apply-header-toggle-box .apply-toggle-btn {
  width: 100px;
  height: 30px;
  position: relative;
  transition: all 0.3s;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 14px;
  cursor: pointer;
  color: grey;
}

.apply-header-toggle-box .all-apply-btn {
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.apply-header-toggle-box .some-apply-btn {
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
}

.on-apply-btn {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff !important;
  background-color: #0088ff !important;
  /* filter: sepia(80); */
  color: #ffffff !important;
}

.apply-container .apply-body {
  margin-top: 10px;
  width: 100%;
  height: 450px;
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  border-radius: 20px;
  overflow: auto;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
}

.applicant-card {
  width: calc(30% - 24px);
  height: 100px;
  margin: 10px 13px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  display: flex;
  padding: 15px;
  cursor: pointer;
}

.applicant-card .applicant-img-box {
  width: 40%;
}

.applicant-card .applicant-img-box > img {
  width: 100%;
  height: 100%;
}

.applicant-card .applicant-text-box {
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.applicant-card .applicant-text-box > p {
  font-size: 12px;
}

.applicant-card .applicant-text-box > p:nth-child(1) {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 5px;
}
</style>