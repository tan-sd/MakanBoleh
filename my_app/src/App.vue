<template>
  <!-- <div id="nav">
    <router-link to="/">Home</router-link>
    <router-link to="/user">User Profile</router-link>
  </div> -->
  <!-- <router-view/> -->
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <button class="btn btn-main-light">Hi There</button> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  <img
      src="./assets/images/logos/small_logos/MakanBoleh_logo_long_light_small.png"
      style="margin-bottom: 10px; width: 25vw;"
    />
  <Map/>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Map from "./components/Map.vue";

export default {
  name: "App",
  components: {
    // HelloWorld,
    Map
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
