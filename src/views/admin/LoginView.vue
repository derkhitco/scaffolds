<template>
    <div class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="w-full max-w-md space-y-8">
            <form class="mt-8 space-y-6" action="#" method="POST">
                <input type="hidden" name="remember" value="true" />
                <div class="-space-y-px rounded-md shadow-sm">
                    <div>
                        <label for="email-address" class="sr-only">Email</label>
                        <input id="email-address" name="email" type="email" autocomplete="email" required="true"
                            v-model="username"
                            class="relative block w-full appearance-none rounded-none rounded-t-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-primary-500 focus:outline-none focus:ring-primary-500 sm:text-sm"
                            placeholder="Email" />
                    </div>
                    <div>
                        <label for="password" class="sr-only">Wachtwoord</label>
                        <input id="password" name="password" type="password" required="true" v-model="password"
                            class="relative block w-full appearance-none rounded-none rounded-b-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-primary-500 focus:outline-none focus:ring-primary-500 sm:text-sm"
                            placeholder="Wachtwoord" />
                    </div>
                </div>

                <div>
                    <button
                        class="group relative flex w-full justify-center rounded-md border border-transparent bg-primary py-2 px-4 text-sm font-medium text-black hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                        @click="login">
                        <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                        </span>
                        Inloggen
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref } from 'vue'
import { useUserStore } from '../../stores/users'

const router = useRouter()

const userStore = useUserStore()
const username = ref()
const password = ref()
function login(e: Event) {
    e.preventDefault();
    userStore.logIn(username.value, password.value).then(resp => {router.push('/admin')})
}

</script>
