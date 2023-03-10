import { createApp } from "vue";
import App from "./App.vue";
import router from './router';
import "../styling/sass/main.min.css";
import "../styling/style.css";

createApp(App).use(router).mount("#app");