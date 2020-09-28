<template>
  <div class="wrap">
    <div class="wrap-container">
      ㅎㅇ
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecruitWrite',
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
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>

<style>

</style>