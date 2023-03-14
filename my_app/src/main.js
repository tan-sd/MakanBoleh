import { createApp } from "vue";
import App from "./App.vue";
import router from './router';
import VueGoogleMaps from '@fawmi/vue-google-maps';
import "../styling/sass/main.min.css";
import "../styling/style.css";

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faBars, faBurger, faCircleArrowRight, faCircleStop, faCow, faHourglassHalf, faLeaf, faLocationDot, faPersonWalking, faPlus, faStarAndCrescent, faUserSecret, faUtensils } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faLocationDot, faStarAndCrescent, faLeaf, faCow, faHourglassHalf, faPlus, faUtensils, faBurger, faBars, faPersonWalking, faCircleArrowRight ,faCircleStop)

import "../node_modules/bootstrap/dist/js/bootstrap"

const app = createApp(App);
app.use(router).use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyB_XNrepzj7pUf2-dp9vSkpAfjXkAB9yHI',
        libraries: 'places'
    },
});

app.component('font-awesome-icon', FontAwesomeIcon);
app.mount("#app");