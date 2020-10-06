<template>
  <div class="wrap recruit-wrap">
    <div class="wrap-container recruit-container">
      <div class="recruit-user-box">
        <div class="recruit-user-content">
          <label for="recruit-user-img-edit">
            <div class="recruit-user-img-box">
              <img v-if='!getData.image' class="default-img" src="@/assets/images/company2.png" alt="#">
              <img v-if='getData.image' :src="getData.image" alt="#">
              <p v-if='!getData.image'>회사로고를 등록해 주세요</p>
              <input type="file" id="recruit-user-img-edit" accept="image/*" @change="setProfileImg">
            </div>
          </label>
          <p class="recruit-user-name">{{ UserInfo.last_name }}</p>
          <p class="recruit-user-email">{{ UserInfo.email }}</p>
          <div class="recruit-user-btn" @click="goRecruitWrite">공고 작성하기</div>
        </div>
      </div>
      <div class="recruit-data-box">
        <div class="recruit-data-content-box">
          <p>작성한공고</p>
          <p v-if="RecruitList.length===0">작성한 공고가 없습니다.</p>
          <div v-for="recruit in RecruitList" :key="recruit.id" @click="onModal(recruit.id)">
            <div class="recruit-data-content" v-if="(recruit.user.email === UserInfo.email)&&(recruit.deadline>nowTime)">
              <div class="recruit-data-head">
                <span class="recruit-data-sort">{{ recruit.division }}</span>
                <span class="recruit-data-name">{{ recruit.title }}</span>
              </div>
              <div class="recruit-data-footer">
                <span>마감일</span>
                <span>{{recruit.deadline.substring(0,4)}}.{{recruit.deadline.substring(4,6)}}.{{recruit.deadline.substring(6,8)}}</span>
                <span>{{ recruit.deadline.substring(8,10) }}:{{ recruit.deadline.substring(10,) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <RecruitModal v-if="showModal" @close="showModal= false"/>
  </div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert';
import { mapState, mapMutations } from 'vuex';
import RecruitModal from '../components/RecruitModal.vue'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'RecruitHome',
  props: {
    first: {
      type: Boolean,
    },
    private_key: {
      type: Object,
    }
  },
  data() {
    return {
      showModal: false,
      test: '',
      getData: [],
      RecruitList: [],
      profileImg: '',
      nowTime: '',
    }
  },
  components: {
    RecruitModal,
  },
  computed: {
    ...mapState(['UserInfo']),
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    this.setNowTime()
    this.getRecruit()
    this.getResume()
    setTimeout(() => {
      this.getResume()
    }, 1000);
    swal(`warning\n`, `${this.private_key.result}\n\n1. 지갑 비밀키를 잃어버리지 마세요! 한 번 잃어버리면 복구 할 수 없습니다.\n2. 공유하지 마세요! 비밀키가 악위적인 사이트에 노출되면 당신의 자산이 유실될 수 있습니다.\n3. 백업을 만들어 두세요! 종이에 적어서 오프라인으로 관리하세요.`, "warning")
  },
  watch: {
  },
  methods: {
    ...mapMutations(['setRecruitId']),
    handleScroll() {
      const ORIGIN = 0
      let TOP = window.scrollY
      document.querySelector('.recruit-user-content').style.top = (ORIGIN + TOP) + 'px';
    },
    goRecruitWrite() {
      this.$router.push('/corp/recruit/write').catch(()=>{})
    },
    setProfileImg() {
      const photoFile = document.getElementById("recruit-user-img-edit");
      this.getData.image = URL.createObjectURL(photoFile.files[0]);
      this.profileImg = photoFile.files[0]
      this.editResume()
    },
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/`, null, config)
      .then(res => {
        console.log(res,'get resume')
        this.getData = res.data
        if(this.getData.image) {
          this.getData.image = 'http://localhost:8000' + this.getData.image
        }
      })
      .catch((err) => console.log(err.response))
    },
    getRecruit() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}recruitments/`, null, config)
      .then(res => {
        console.log(res,'get recruitment')
        this.RecruitList = res.data
      })
      .catch((err) => console.log(err.response))
    },
    editResume() {
      let data = new FormData();
      data.append('image', this.profileImg);
      for (var key of data.keys()) {console.log(key);}
      for (var value of data.values()) {console.log(value);}
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if (this.profileImg) {
        axios.put(`${SERVER_URL}articles/${this.UserInfo.id}/`, data, config)
        .then(res => {
          console.log(res,'put resume image')
        })
        .catch((err) => console.log(err.response))
      }
    },
    onModal(id) {
      this.setRecruitId(id)
      this.showModal = true;
    },
    setNowTime() {
      let today = new Date();   
      let year = today.getFullYear()
      let month = today.getMonth()+1
      let date = ''+today.getDate()
      let hours = today.getHours()
      let minutes = today.getMinutes()
      if(month.length === 1) {
        month = '0' + month
      }
      if (date.length === 1) {
        date = '0' + date
      }
      this.nowTime = year + '' + month + '' + date + '' + hours + '' + minutes
      console.log(this.nowTime)
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

.recruit-user-img-box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  flex-direction: column;
  position: relative;
  cursor: pointer;
}

.recruit-user-img-box > .default-img {
  width: 150px !important;
  height: 150px !important;
}

.recruit-user-img-box > img {
  width: 86%;
  padding: 7%;
}

.recruit-user-img-box > p {
  font-size: 12px;
  position: absolute;
  bottom: 13px;
  font-weight: 900;
}

.recruit-user-img-box input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
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

.recruit-data-content-box > p:nth-child(2) {
  font-size: 13px;
  font-family: "Noto Sans KR", sans-serif !important;
  margin-left: 250px;
  font-weight: 400;
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