import { createRouter as _createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from './stores/users'
import AdminWrapper from './components/wrappers/AdminWrapper.vue'
import SiteWrapper from './components/wrappers/SiteWrapper.vue'

// Site imports (do not remove this line)
import Home from './views/site/Home.vue'
import About from './views/site/About.vue'

import Login from './views/app/Login.vue'

// Admin imports (do not remove this line)
import EditHome from './views/app/EditHome.vue'
import EditAbout from './views/app/EditAbout.vue'
import AdminHome from './views/app/Index.vue'

const routes = [
    {
        path: '/',
        name: 'SiteWrapper',
        component: SiteWrapper,
        children: [
            // placeholder for adding site children. Do not remove
            {
                path: '',
                name: 'Index',
                component: Home,
                meta: { inHeader: false }
            },
            {
                path: 'about',
                name: 'About',
                component: About,
                meta: { inHeader: true }
            }
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/admin/',
        name: 'AdminWrapper',
        component: AdminWrapper,
        meta: { auth: true },
        children: [
            // placeholder for adding admin children. Do not remove
            {
                path: '',
                name: 'Admin index',
                component: AdminHome,
                meta: {inHeader: false}
            },
            {
                path: 'home',
                name: 'Home pagina',
                component: EditHome,
                meta: { inHeader: true }
            },
            {
                path: 'about',
                name: 'About pagina',
                component: EditAbout,
                meta: { inHeader: true }
            }
        ]
    },
]

function createRouter() {
    return _createRouter({
        history: createWebHistory(import.meta.env.BASE_URL),
        routes,
        scrollBehavior(to, from, savedPosition) {
            return { top: 0 }
        }
    })
}

async function authenticate(to: any, from: any) {
    const userStore = useUserStore()
    const currentUser = await userStore.getuserInit()
    if (to.meta?.auth && !currentUser) {
        // return { name: 'Login' }
    }
};


export { createRouter, authenticate, routes }