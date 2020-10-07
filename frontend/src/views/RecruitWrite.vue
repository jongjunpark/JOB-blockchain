<template>
  <div class="wrap">
    <div class="wrap-container">
      <div class="recruit-write-btn-box">
        <div v-if="!isRecruit" class="recruit-write-btn">작성하기</div>
        <div v-if="isRecruit" class="recruit-write-btn on-write-btn" @click="editRecruit">작성하기</div>
      </div>
      <div class="recruit-write-box">
        <p>기본정보</p>
        <div class="recruit-write-inner-box">
          <label for="">공고명</label><input type="text" v-model="recruit.name" v-on:input="recruit.name = $event.target.value">
          <label for="">구분</label>
          <select name="" id="" v-model='recruit.sort'>
            <option disabled selected>선택</option>
            <option>신입</option><option>경력</option><option>신입/경력</option>
          </select>
        </div>
        <div class="recruit-write-inner-box">
          <label for="">공고자료</label>
          <label for="recruit-write-file" class="recruit-write-file-form">첨부하기</label><input type="file" ccept="image/*" id="recruit-write-file" @change="setImg">
          <span>{{ imgName }}</span>
        </div>
        <div class="recruit-write-inner-box recruit-write-inner-time">
          <label for="">시작시간</label><input type="text" class="long-width" placeholder="YYYY.MM.DD" v-model="recruit.startDate">
          <input type="text" class="short-width" placeholder="HH" v-model="recruit.startHour"><input type="text" class="short-width" placeholder="MM" v-model="recruit.startMin">
          <div></div>
          <label for="">마감시간</label><input type="text" class="long-width" placeholder="YYYY.MM.DD" v-model="recruit.endDate">
          <input type="text" class="short-width" placeholder="HH" v-model="recruit.endHour"><input type="text" class="short-width" placeholder="MM" v-model="recruit.endMin">
        </div>
      </div>
      <div class="recruit-write-box">
        <p>자기소개서</p>
        <div class="recruit-write-certified-box">
          <p v-if="certifiedSelf.length === 0">자기소개서 양식을 입력해주세요.</p>
          <div class='recruit-write-self-list-box' v-for='(self, index) in certifiedSelf' :key='`self-${index}`'>
            <div class="self-detail">{{ index+1 }}.</div>
            <div class="self-detail">{{ self[0] }}</div>
            <div class="self-detail">{{ self[1] }}자</div>
            <div class="self-detail self-del-box" @click="delSelf(index)">x</div>
          </div>
        </div>
        <div class="recruit-write-inner-box recruit-write-selfintro">
          <label for="">제목</label><input type="text" v-model="self.name">
          <label for="">글자수</label><input type="text" v-model="self.length">
        </div>
        <div class="recruit-write-btn-area">
          <div v-if="isSelf" class="recruit-write-self-btn on-write-btn" @click="addSelf">추가하기</div>
          <div v-if="!isSelf" class="recruit-write-self-btn">추가하기</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'RecruitWrite',
  data() {
    return {
      imgName: '공고 이미지를 첨부해주세요',
      recruit: {
        name: '',
        sort: '선택',
        img: '',
        startDate: '',
        startHour: '',
        startMin: '',
        endDate: '',
        endHour: '',
        endMin: '',
        id: '',
      },
      self: {
        name: '',
        length: '',
      },
      isSelf: false,
      isRecruit: false,
      certifiedSelf: [],
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
    self: {
      handler() {
        this.checkSelfForm();
        this.checkWriteForm();
      }, deep:true
    },
    recruit: {
      handler() {
        this.checkWriteForm();
      }, deep:true
    },
    certifiedSelf() {
      this.checkWriteForm();
    }
  },
  methods: {
    handleScroll() {
      const ORIGIN = -600
      let TOP = window.scrollY
      document.querySelector('.recruit-write-btn').style.bottom = (ORIGIN - TOP) + 'px';
    },
    setImg() {
      const photoFile = document.getElementById("recruit-write-file");
      this.imgName = photoFile.files[0].name
      this.recruit.img = photoFile.files[0]
    },
    editRecruit() {
      this.splitDate()
      let data = new FormData();
      data.append('image', this.recruit.img);
      data.append('division', this.recruit.sort);
      data.append('title', this.recruit.name);
      data.append('startdate', this.recruit.startDate + this.recruit.startHour + this.recruit.startMin)
      data.append('deadline', this.recruit.endDate + this.recruit.endHour + this.recruit.endMin)
      for (var key of data.keys()) {console.log(key);}
      for (var value of data.values()) {console.log(value);}
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}recruitments/create/`, data, config)
      .then(res => {
        console.log(res,'create recruit')
        axios.get(`${SERVER_URL}recruitments/`, null, config)
        .then(res => {
          console.log(res)
          this.recruit.id = res.data[res.data.length-1].id
          // 리스트에서 마지막 배열의 id를 받아와야함
          for (let i=0; i<this.certifiedSelf.length; i++) {
            axios.post(`${SERVER_URL}recruitments/${this.recruit.id}/introductions/create/`, {
              title : this.certifiedSelf[i][0],
              number : this.certifiedSelf[i][1],
              recruitment : this.recruit.id
            }, config)
            .then(res => {
              console.log(res,'create self')
              this.$router.push('/corp/recruit').catch(()=>{})
            })
            .catch((err) => console.log(err.response))
          }
        })
        .catch((err) => console.log(err.response))
      })
      .catch((err) => console.log(err.response))
    },
    checkSelfForm() {
      if (this.self.name && this.self.length) {
        this.isSelf = true
      } else {
        this.isSelf = false
      }
    },
    checkWriteForm() {
      if (this.recruit.name && (this.recruit.sort && this.recruit.sort != '선택') && this.recruit.img
      && this.recruit.startDate && this.recruit.startHour && this.recruit.startMin
      && this.recruit.endDate && this.recruit.endHour && this.recruit.endMin && this.certifiedSelf[0]) {
        this.isRecruit = true
      } else {
        this.isRecruit = false
      }
    },
    addSelf() {
      let ARR = []
      ARR.push(this.self.name); ARR.push(this.self.length);
      this.certifiedSelf.push(ARR)
      this.self.name = ''; this.self.length = '';
    },
    delSelf(idx) {
      this.certifiedSelf.splice(idx, 1);
    },
    splitDate() {
      const arr = this.recruit.startDate.split('.')
      const arr2 = this.recruit.endDate.split('.')
      this.recruit.startDate = ''
      this.recruit.endDate = ''
      for(let i=0; i<arr.length; i++) {
        this.recruit.startDate += arr[i]
      }
      for(let j=0; j<arr.length; j++) {
        this.recruit.endDate += arr2[j]
      }
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>
.recruit-write-btn-box {
  position: relative;
  width: 100%;
}

.recruit-write-btn {
  position: absolute;
  bottom: -600px;
  right: -80px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 50px;
  border-radius: 30px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  transition: box-shadow .3s;
  color: rgba(0,0,0,0.3);
}

.recruit-write-btn-box .on-write-btn {
  background-color: #0088ff;
  cursor: pointer;
  color: #ffffff;
}

.recruit-write-btn-box .on-write-btn:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  font-weight: 700;
}

.recruit-write-box {
  width: 50%;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  margin-top: 40px;
  padding: 20px 40px 20px 40px;
}

.recruit-write-box > p {
  font-family: 'TmonMonsori';
  margin-bottom: 30px;
  font-weight: 500;
  font-size: 28px;
}

.recruit-write-box .recruit-write-inner-box {
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.recruit-write-inner-box label {
  margin-right: 10px;
  font-size: 15px;
  font-weight: 700;
  width: 60px;
  display: flex;
  justify-content: flex-end;
}

.recruit-write-inner-box input[type='text'] {
  width: 350px;
  height: 30px;
  padding-left: 15px;
  padding-right: 15px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border: none;
  border-radius: 20px;
  outline: none;
  background: transparent;
  font-size: 12px;
}

.recruit-write-inner-box input[type='text']::placeholder {
  font-size: 11px;
  text-align: center;
}

.recruit-write-inner-box select {
  width: 140px;
  height: 30px;
  padding-left: 15px;
  padding-right: 15px;
  margin-right: 20px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border: none;
  border-radius: 20px;
  outline: none;
  background: transparent;
}

.recruit-write-inner-box input[type='file'] {
  position: absolute; 
  width: 1px; 
  height: 1px; 
  padding: 0; 
  margin: -1px; 
  overflow: hidden; 
  clip:rect(0,0,0,0); 
  border: 0;
}

.recruit-write-file-form {
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 10px;
  padding: 5px 10px;
  font-weight: 300 !important;
  font-size: 12px !important;
  transition: all .3s;
  cursor: pointer;
  display: flex;
  justify-content: center !important;
  align-items: center;
  width: 50px !important;
  margin-right: 0 !important;
}

.recruit-write-file-form:hover {
  background-color: #ececf0 !important;
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff !important;
}

#upload-name {
  border: none;
}

.recruit-write-inner-box > span {
  font-size: 12px;
  margin-left: 10px;
  color: rgba(0,0,0,0.7)
}

.recruit-write-inner-time .long-width {
  width: 70px !important;
  margin-right: 5px;
}

.recruit-write-inner-time .short-width {
  width: 20px !important;
  margin-right: 5px;
}

.recruit-write-inner-time > div {
  margin-right: 70px;
}

.recruit-write-selfintro > input:nth-child(4) {
  width: 70px !important;
}

.recruit-write-box .recruit-write-certified-box {
  width: 92%;
  padding: 20px 4%;
  /* background-color: aqua; */
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.recruit-write-box .recruit-write-certified-box > p {
  font-size: 12px;
}


.recruit-write-box .recruit-write-btn-area {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  margin-top: 40px;
}

.recruit-write-btn-area .recruit-write-self-btn {
  width: 200px;
  height: 45px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 30px;
  transition: all .5s;
  color: rgba(0,0,0,0.4);
}

.recruit-write-btn-area .on-write-btn {
  cursor: pointer;
  background-color: #0088ff;
  color: #ffffff !important;
  transition: box-shadow .5s;
  cursor: pointer;
}

.recruit-write-btn-area .on-write-btn:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  font-weight: 700;
}

.recruit-write-certified-box .recruit-write-self-list-box {
  width: 100%;
  /* background-color: aqua; */
  display: flex;
  margin: 5px 0;
}

.recruit-write-self-list-box .self-detail {
  font-size: 12px;
  margin-right: 5px;
}

.recruit-write-self-list-box .self-del-box {
  border-radius: 50%;
  width: 18px;
  height: 18px;
  display: flex;
  justify-content: center;
  line-height: 1.4;
  margin-left: 5px;
  /* align-items: center; */
  background-color: rgb(255, 50, 50);
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  color: #ffffff;
  cursor: pointer;
  transition: .3s;
}

.recruit-write-self-list-box .self-del-box:hover {
  background-color: rgb(221, 50, 50);
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 2px 2px 6px -1px rgba(0,0,0,0.2),
              inset -1px -1px 4px -1px #ffffff;
}
</style>