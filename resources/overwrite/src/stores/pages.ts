import { defineStore } from 'pinia'
import { reloadStorageRefs, uploadFiles, cleanEmptyRefs } from '../util/files'
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import { Pages } from '../util/types'
import { ref as dbref, getDatabase, set, onValue } from "firebase/database";

export const usePageStore = defineStore('pages', () => {
    const texts: Ref<Pages> = ref(
        {
            // default values, do not remove this line
		overOns: {title: ''},
		sustainable: {title: ''},
            home: { title: '', description: '', text: '' },
            about: { title: '', description: '', text: '' }
        }
    )

    const db = getDatabase();
    const textsPath = 'pages/'
    const textsRef = dbref(db, textsPath)

    // computed pages, do not remove this line
	const overOns = computed(() => texts.value.overOns)
	const sustainable = computed(() => texts.value.sustainable)
    const home = computed(() => texts.value.home)
    const about = computed(() => texts.value.about)

    async function save() {
        texts.value = cleanEmptyRefs(texts.value)
        uploadFiles(texts.value, textsPath).then(() => {
            set(textsRef, texts.value);
            return true
        }).catch((error) => { return false })
    }

    onValue(textsRef, async (snapshot) => {
        const newValue = await reloadStorageRefs(snapshot.val())
        for (const key in newValue) {
            texts.value[key as keyof Pages] = newValue[key]
        }
    });

    
    return {
        // return statement, do not remove this line
		overOns,
		sustainable,
        home,
        about,
        save
    }
}
)

