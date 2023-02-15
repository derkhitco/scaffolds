// import { createApp } from 'vue'
// import { createRouter, authenticate } from './router'
// import { createPinia } from 'pinia'

// import App from './App.vue'

// const router = createRouter()
// router.beforeEach(authenticate)

// const codeSiteName = siteName.replace(/ /g, '_').toLowerCase()


// createApp(App).use(createPinia()).use(router).mount('#app')

// export { firebaseApp, codeSiteName as siteName }

import './style.css'
import App from './App.vue'
import { routes, authenticate } from './router'
import viteSSR from 'vite-ssr'
import { pinia } from './pinia'
import devalue from '@nuxt/devalue'

const siteName = 'Sample App'

export default viteSSR(
    App,
    {
        routes,
        transformState(state) {
            return import.meta.env.SSR ? devalue(state) : state
        },
    },
    ({ initialState, router, app }) => {
        // ...
        if (import.meta.env.SSR) {
            // this will be stringified and set to window.__INITIAL_STATE__
            initialState.pinia = pinia.state.value
        } else {
            // on the client side, we restore the state
            pinia.state.value = initialState.pinia
        }
        app.use(pinia)
        router.beforeEach(authenticate)
    }
)

export { siteName }