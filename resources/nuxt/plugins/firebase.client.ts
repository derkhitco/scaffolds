
import { initializeApp } from 'firebase/app'
import { getAuth } from "firebase/auth"
import { getAnalytics } from "firebase/analytics"
import { getFunctions, connectFunctionsEmulator } from 'firebase/functions';

export default defineNuxtPlugin(nuxtApp => {
    const config = useRuntimeConfig()

    const firebaseConfig = {%FBCONFIG%};

    const app = initializeApp(firebaseConfig)
    const analytics = getAnalytics(app)
    const functions = getFunctions(app);
    const auth = getAuth(app)

    if (process.env.NODE_ENV === 'local') {
        connectFunctionsEmulator(functions, 'localhost', 5001);
    }

    nuxtApp.vueApp.provide('auth', auth)
    nuxtApp.provide('auth', auth)

    nuxtApp.vueApp.provide('functions', functions)
    nuxtApp.provide('functions', functions)
})
