import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, setPersistence, signOut } from "firebase/auth";
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('users', () => {
    const auth = getAuth();
    const user = ref(auth.currentUser)

    onAuthStateChanged(auth, newUser => { user.value = newUser })

    function logOut() {
        signOut(auth)
    }

    async function logIn(email: string, password: string) { return signInWithEmailAndPassword(auth, email, password) }

    async function getuserInit() {
        return new Promise((resolve, reject) => {
            const unsubscribe = onAuthStateChanged(auth, (user) => {
                if (user) {
                    unsubscribe()
                    resolve(user)
                }
                else {
                    unsubscribe();
                    resolve(null)
                }
            }, reject);
        })
    }

    return { logIn, logOut, getuserInit, user }
})