import { createApp } from "vue";
import App from "./App.vue";
import "../styling/sass/main.min.css";
import "../styling/style.css"

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faBars, faBurger, faCow, faHourglassHalf, faLeaf, faLocationDot, faPersonWalking, faPlus, faStarAndCrescent, faUserSecret, faUtensils } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faLocationDot, faStarAndCrescent, faLeaf, faCow, faHourglassHalf, faPlus, faUtensils, faBurger, faBars, faPersonWalking)

createApp(App).component('font-awesome-icon', FontAwesomeIcon).mount("#app");

import "../node_modules/bootstrap/dist/js/bootstrap"