import { createRouter, createWebHistory } from "vue-router";
import Home from '../views/Home.vue'
import About from '../views/UserProfile.vue'

const routes = [
    {
        path: '/',
        name: 'MakanBoleh',
        component: Home
    },
    {
        path: '/user',
        name: 'User',
        component: About
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    document.title = to.name;
    next();
});

export default router