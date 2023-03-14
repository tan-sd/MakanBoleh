<template>
  <NavBar/>
  <!-- <Map/> -->
  <!-- <FoodList/> -->
  <router-view></router-view>
</template>

<script>
// import Map from "./components/Map.vue";
import NavBar from "./components/NavBar.vue";
// import FoodList from "./components/FoodList.vue";

export default {
  name: "App",
  components: {
    // Map,
    NavBar,
    // FoodList
  },
};
</script>