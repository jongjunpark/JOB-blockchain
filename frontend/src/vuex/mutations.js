export default {
  setIsLogin(state, data) {
    state.isLogin = data
  },
  setMailInput(state, data) {
    state.signUpInput = data
  },
  setMailCode(state, data) {
    state.mailCode = data
  },
  setMailValid(state, data) {
    state.mailValid = data
  },
  setIsLoggedIn(state, data) {
    state.isLoggedIn = data
  },
  setToken(state, data) {
    state.authToken = data
  }
}