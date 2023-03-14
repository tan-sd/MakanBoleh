<template>
    <Map/>
    <FoodList/>
  </template>
  
  <script>
  import Map from "../components/Map.vue";
  import FoodList from "../components/FoodList.vue";
  
  export default {
    name: "App",
    components: {
      Map,
      FoodList
    },
  };
  </script>