<template>
  <div id="app">
    <div id="nav">
    </div>
    <router-view/>
  </div>
</template>

<script>
import "../public/css/common.css";
export default {
  name: 'App'
}
</script>

<style>
  #nav {
    height: 7vh;
    min-height: 30px;
    background-color: #eff0f5;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),
                -6px -6px 10px -1px rgba(255,255,255,0.7);
    border: 1px solid rgba(0,0,0,0);
    z-index: 5000;
  }
</style>
