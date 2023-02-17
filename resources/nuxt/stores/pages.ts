import { defineStore } from 'pinia'
import { reloadStorageRefs, uploadFiles, cleanEmptyRefs } from '../util/files'
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import { Pages } from '~/util/types'
import { ref as dbref, getDatabase, set, get, onValue } from "firebase/database";

export const usePageStore = defineStore('pages', () => {

    const pages: Ref<Pages> = ref({
        // default values, do not remove this line
        home: { title: '', description: '', text: '' },
        about: { title: '', description: '', text: '' }
    })

    const db = getDatabase();
    const textsPath = 'pages/'
    const textsRef = dbref(db, textsPath)

    // computed pages, do not remove this line
    const home = computed(() => pages.value.home)
    const about = computed(() => pages.value.about)

    async function save() {
        uploadFiles(pages.value, textsPath).then(() => {
            pages.value = cleanEmptyRefs(pages.value)
            set(textsRef, pages.value);
            return true
        }).catch((error) => {
            console.log(error)
            return false
        })
    }

    onValue(textsRef, async (snapshot) => {
        const newValue = await reloadStorageRefs(snapshot.val())
        for (const key in newValue) {
            pages.value[key as keyof Pages] = newValue[key]
        }
    });


    useAsyncData(async () => {
        const snapshot = await get(textsRef)
        const newValue = await reloadStorageRefs(snapshot.val())
        for (const key in pages.value) {
            if (newValue[key] === undefined) newValue[key] = pages.value[key as keyof Pages]
        }
        pages.value = newValue as Pages
    })

    return {
        // return statement, do not remove this line
        home,
        about,
        save
    }
}
)

