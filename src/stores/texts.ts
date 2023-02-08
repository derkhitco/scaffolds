import { defineStore } from 'pinia'
import { reloadStorageRefs, uploadFiles } from '../util/files'
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import { Texts } from '../util/types'
import { ref as dbref, getDatabase, set, onValue } from "firebase/database";

export const useTextStore = defineStore('texts', () => {
    const texts: Ref<Texts> = ref({})

    const db = getDatabase();
    const textsPath = 'texts/'
    const textsRef = dbref(db, textsPath)

    const home = computed({
        get: () => texts.value.home,
        set: (value) => { texts.value.home = value }
    })

    async function save() {
        await uploadFiles(texts.value, textsPath)
        set(textsRef, texts.value);
        console.log('Saved texts')
    }

    onValue(textsRef, async (snapshot) => {
        texts.value = await reloadStorageRefs(snapshot.val())
    });

    return { home, save }
}
)

