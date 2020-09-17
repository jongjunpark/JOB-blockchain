<template>
  <transition name="modal">
    <div class="school-search-modal-mask">
      <div class="school-search-modal-wrap">
        <div class="school-search-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div class='school-search-modal-header'>학교검색</div>
          <div class='school-search-modal-body'>
            <input v-model="name" class='school-search-valid-input' type="text" v-on:input="name = $event.target.value" @keydown.enter="getSchool(schoolType, name, schoolDetail)">
            <div class="school-submit-btn" @click="getSchool(schoolType, name, schoolDetail)">검색</div>
          </div>
          <div class="school-search-modal-footer">
            <span class='school-search-list' v-for='(school, index) in schoolList' :key='`school-${index}`' @click="setSchool(school, schoolType2)">
              {{ school }}
            <br>
            </span>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import axios from 'axios'

// const SERVER_URL = 'http://127.0.0.1:8000/'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'SchoolSearch',
  data() {
    return {
      name: '',
      schoolList: [],
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['schoolType', 'schoolType2', 'schoolName', 'schoolDetail']),
  },
  created() {
    this.name = this.schoolName
    this.getSchool(this.schoolType, this.schoolName, this.schoolDetail)
  },
  mounted() {
    
  },
  methods: {
    ...mapMutations(['selectSchool', 'selectSchoolType']),
    getSchool(type, name, num) {
      if (num === 0) {
        axios.get('http://www.career.go.kr/cnet/openapi/getOpenApi', {
        params: {
          apiKey: API_KEY,
          svcType: 'api',
          svcCode: 'SCHOOL',
          gubun: type,
          searchSchulNm: name,
          contentType: 'json'
        }
      }).then(res => {
        let ARR = []
        for (let i=0; i<res.data.dataSearch.content.length ; i++) {
          ARR.push(res.data.dataSearch.content[i].schoolName)
        }
        this.schoolList = Array.from(new Set(ARR))
        console.log(this.schoolList)
      })
      .catch(err =>{
        console.log(err.response)
      })
    } else {
      axios.get('http://www.career.go.kr/cnet/openapi/getOpenApi', {
        params: {
          apiKey: API_KEY,
          svcType: 'api',
          svcCode: 'SCHOOL',
          gubun: type,
          searchSchulNm: name,
          sch1: num,
          contentType: 'json'
        }
      }).then(res => {
        let ARR = []
        for (let i=0; i<res.data.dataSearch.content.length ; i++) {
          ARR.push(res.data.dataSearch.content[i].schoolName)
        }
        this.schoolList = Array.from(new Set(ARR))
        console.log(this.schoolList)
      })
      .catch(err =>{
        console.log(err.response)
      })
    }
      
    },
    setSchool(name, type) {
      this.selectSchool(name)
      this.selectSchoolType(type)
      this.$emit('close')
    }
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

.school-search-modal-mask {
  position: fixed;
  z-index: 99999;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.school-search-modal-mask .fa-times {
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
  color: rgba(0,0,0,0.8);
  font-size: 25px;
  transition: all .3s;
}

.school-search-modal-mask .fa-times:hover {
  color: #0088ff;
}

.modal-enter .school-search-modal-wrapper,
.modal-leave-active .school-search-modal-wrapper {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.school-search-modal-wrap {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  padding: 1vh;
  transition: 0.3s ease;
  background-color: #eff0f5;
  border-radius: 1vw;
  width: 88%
}

@media (min-width: 450px) {
  .school-search-modal-wrap {
  max-width: 50vh;
  width: 100%;
  margin: 0 auto;
  }
}

.school-search-modal-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px;
}


.school-search-modal-content .school-search-modal-header {
  width: 100%;
  font-size: 30px;
  font-weight: 700;
  margin: 20px 0;
}

.school-search-modal-content .school-search-modal-body {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.school-search-modal-body .school-search-valid-input {
  width: 65%;
  height: 40px;
  padding-left: 6%;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -4px -4px 6px -1px #ffffff;
  border: 0px solid rgba(0,0,0,0);
  border-radius: 20px;
  outline: none;
  margin-bottom: 20px;
  background: transparent;
}

.school-search-modal-body .school-submit-btn {
  width: 25%;
  height: 40px;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all .5s;
}

.school-search-modal-body .school-submit-btn:hover {
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff !important;
  background-color: #0088ff;
  font-weight: 700;
  color: #ffffff !important;
}

.school-search-modal-content .school-search-modal-footer {
  width: calc(100% - 40px);
  padding: 10px 20px;
  box-shadow: 0 0 0 0 rgba(0,0,0,0),
              0 0 0 0 rgba(0,0,0,0),
              inset 4px 4px 6px -1px rgba(0,0,0,0.2),
              inset -3px -3px 4px -1px #ffffff;
  border-radius: 20px;
  height: 100px;
  overflow: auto;
}

.school-search-modal-footer .school-search-list {
  cursor: pointer;
  color: rgba(0,0,0,0.7);
  transition: all .4s;
}

.school-search-modal-footer .school-search-list:hover {
  color: #0088ff;
}
</style>
