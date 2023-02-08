import { createRouter as _createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from './stores/users'

import WrapperView from './views/WrapperView.vue'
import HomeView from './views/IndexView.vue'

import LoginView from './views/admin/LoginView.vue'
import AdminWrapperView from './views/admin/WrapperView.vue'
import HomePageAdmin from './views/admin/HomePageAdmin.vue'
import AdminView from './views/admin/IndexView.vue'

const routes = [
    {
        path: '/',
        name: 'Wrapper',
        component: WrapperView,
        children: [
            {
                path: '',
                name: 'Home',
                component: HomeView
            }
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView
    },
    {
        path: '/admin',
        name: 'AdminWrapper',
        component: AdminWrapperView,
        meta: { auth: true },
        children: [
            {
                path: '/admin/home',
                name: 'HomePageAdmin',
                component: HomePageAdmin,
                meta: { auth: true }
            },
            {
                path: '/admin',
                name: 'AdminIndex',
                component: AdminView,
                meta: { auth: true }
            }
        ]
    }
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
        return { name: 'Login' }
    }
};


export { createRouter, authenticate }