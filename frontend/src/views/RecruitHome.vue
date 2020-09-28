<template>
  <div class="wrap recruit-wrap">
    <div class="wrap-container recruit-container">
      <div class="recruit-user-box">
        <div class="recruit-user-content">
          <img src="@/assets/images/default-user.png" alt="#">
          <p class="recruit-user-name">한국전자</p>
          <p class="recruit-user-email">poiufgin7373@naver.com</p>
          <div class="recruit-user-btn" @click="goRecruitWrite">공고 작성하기</div>
        </div>
      </div>
      <div class="recruit-data-box">
        <div class="recruit-data-content-box">
          <p>작성한공고</p>
          <div class="recruit-data-content">
            <div class="recruit-data-head">
              <span class="recruit-data-sort">경력</span>
              <span class="recruit-data-name">물류 경력사원 채용</span>
            </div>
            <div class="recruit-data-footer">
              <span>마감일</span>
              <span>2020.11.01</span>
              <span>18:00</span>
            </div>
          </div>
          <div class="recruit-data-content">
            <div class="recruit-data-head">
              <span class="recruit-data-sort">경력</span>
              <span class="recruit-data-name">물류 경력사원 채용</span>
            </div>
            <div class="recruit-data-footer">
              <span>마감일</span>
              <span>2020.11.01</span>
              <span>18:00</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecruitHome',
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
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.recruit-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    goRecruitWrite() {
      this.$router.push('/corp/recruit/write').catch(()=>{})
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>
.recruit-wrap {
  padding: 0 100px !important;
  width: 1000px !important;
}

.recruit-container {
  flex-direction: row;
}

.recruit-container .recruit-user-box {
  width: 25%;
  height: 30px;
  position: relative;
  /* background-color: hotpink; */
}

.recruit-user-box .recruit-user-content {
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

.recruit-user-content > img {
  width: 100%;
  height: 200px;
}

.recruit-user-content > p {
  margin: 5px 0;
  font-size: 12px;
}

.recruit-user-content > p:nth-child(2) {
  font-size: 20px;
  font-weight: 700;
}

.recruit-user-content .recruit-user-btn {
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

.recruit-user-content .recruit-user-btn:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  font-weight: 700;
}

.recruit-container .recruit-data-box {
  width: 75%;
  height: 30px;
  /* background-color: greenyellow; */
}


.recruit-data-box .recruit-data-content-box {
  width: calc(100% - 100px);
  margin: 30px 0 30px 20px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  padding: 20px 40px 30px 40px;
}

.recruit-data-content-box > p {
  font-family: 'TmonMonsori';
  margin-bottom: 20px;
  font-weight: 500;
  font-size: 25px;
}

.recruit-data-content-box .recruit-data-content {
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  background-color: #eff0f5;
  display: flex;
  padding: 20px;
  justify-content: space-between;
  cursor: pointer;
  transition: all 0.3s;
  margin: 10px 0;
}
.recruit-data-content-box .recruit-data-content:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  background-color: #ececf0;
}

.recruit-data-content .recruit-data-sort {
  padding: 5px 10px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  background-color: #ffffff75;
  margin-right: 10px;
  font-size: 14px;
}

.recruit-data-content .recruit-data-name {
  font-size: 14px;
  font-weight: 700;
}

.recruit-data-content .recruit-data-footer span {
  font-size: 14px;
}

.recruit-data-content .recruit-data-footer span:nth-child(1) {
  margin-right: 10px;
}

.recruit-data-content .recruit-data-footer span:nth-child(2) {
  margin-right: 5px;
  color: rgba(0,0,0,0.7)
}

.recruit-data-content .recruit-data-footer span:nth-child(3) {
  color: rgba(0,0,0,0.7)
}
</style>