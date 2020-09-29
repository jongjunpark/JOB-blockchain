import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'

const state = {
  isLogin: false,
  authToken: '',
  isLoggedIn: false,
  UserInfo: '',
  signUpInput: '',
  mailCode: '',
  mailValid: false,
  loginPath: '',
  schoolName: '',
  schoolType: '',
  schoolTypr2: '',
  schoolDetail: '',
  selectedSchool: '',
  selectedSchoolType: '',
  majorName: '',
  majorType: '',
  majorType2: '',
  selectedMajor: '',
  selectedMajorType: '',
  selectedMajorType2: '',
}

Vue.use(Vuex)

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})

