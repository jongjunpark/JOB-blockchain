import axios from 'axios';
const SERVER_URL = 'http://127.0.0.1:8000/';

export default {
  setUserInfo(context) {
    console.log('sdsdsdsdsd')
    if (context.state.authToken) {
      const config = {
        headers: {
          Authorization: `Token ${context.state.authToken}`
        },
      }
      axios.post(`${SERVER_URL}accounts/`, null, config)
      .then((res)=>{
        context.commit('setUser',res.data)
      })
      .catch(()=>{
      }); 
    } else {
      context.commit('setUser', '')
    }
  },
}
