import { createApp } from 'vue'
import './style.css'
import { createRouter, authenticate } from './router'
import { createPinia } from 'pinia'
import { initializeApp } from "firebase/app";
import { firebaseConfig } from './firebase'
const firebaseApp = initializeApp(firebaseConfig);

import App from './App.vue'

const router = createRouter()
router.beforeEach(authenticate)

createApp(App).use(createPinia()).use(router).mount('#app')

export { firebaseApp }