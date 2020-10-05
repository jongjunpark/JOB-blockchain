<template>
  <div>
    List!
  </div>
</template>

<script>
import '../components/css/login.css'
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'MyList',
  data() {
    return { 
    }
  },
  components: {
  },
  computed: {
  },
  created() {
  },
  mounted() {
    const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
    axios.post(`${SERVER_URL}accounts/`, null, config)
        .then((res) => {
          console.log(res.data)
        })
        .catch(err => {
          console.log(err.response)
        })
  },
  watch: {
  },
  methods: {

  },
}
</script>

<style>

</style>