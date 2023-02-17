import { signInWithEmailAndPassword, signOut } from "firebase/auth";
import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { User } from 'firebase/auth'

export const useUserStore = defineStore('users', () => {
    const { $auth } = useNuxtApp()
    const user: Ref<User | undefined> = computed(() => $auth.currentUser)

    function logOut() { signOut($auth) }
    async function logIn(email: string, password: string) { return signInWithEmailAndPassword($auth, email, password) }

    return { logIn, logOut, user }
})