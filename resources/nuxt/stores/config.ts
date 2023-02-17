import { defineStore } from 'pinia'
import { RemovableRef, useStorage as _useStorage } from '@vueuse/core'
import { ref, computed } from 'vue'
import { Analytics, getAnalytics } from "firebase/analytics";
import { logEvent as _logEvent } from "firebase/analytics";
import { firebaseApp } from './../firebase';
import type { Ref } from 'vue';

import { ConfigStatus } from '../util/types';
import { browserLocalPersistence, inMemoryPersistence } from "firebase/auth";


export const useConfigStore = defineStore('config', () => {

    const siteName = 'SiteName'

    // Everything for remembering the user's choices about privacy
    let localStorage: RemovableRef<ConfigStatus | Object> = _useStorage(`${siteName}.config`, {})
    let analytics: Analytics

    const currentStatus: Ref<ConfigStatus> = ref({
        cookiesStatus: true,
        localStorageStatus: true,
        trackingStatus: true,
        showModalStatus: true
    })

    if (Object.keys(localStorage.value).length !== 0) currentStatus.value = localStorage.value as ConfigStatus

    function syncLocalStorage() {
        if (currentStatus.value.localStorageStatus) localStorage.value = currentStatus.value
        else localStorage.value = {}
    }

    function toggleStatus(key: keyof ConfigStatus, status: boolean) {
        currentStatus.value[key] = status
        syncLocalStorage()
    }

    const cookies = computed({
        get() {
            return currentStatus.value.cookiesStatus
        }, set(val) {
            toggleStatus('cookiesStatus', val)
        }
    })

    const storage = computed({
        get() {
            return currentStatus.value.localStorageStatus
        }, set(val) {
            toggleStatus('localStorageStatus', val)
        }
    })

    const tracking = computed({
        get() {
            return currentStatus.value.trackingStatus
        }, set(val) {
            toggleStatus('trackingStatus', val)
            if (val && !analytics) analytics = getAnalytics(firebaseApp);
        }
    })

    const showOptions = computed({
        get() {
            return currentStatus.value.showModalStatus
        }, set(val) {
            toggleStatus('showModalStatus', val)
        }
    })

    function acceptAll() {
        cookies.value = true
        storage.value = true
        tracking.value = true
        showOptions.value = false
    }

    function saveCurrent() {
        showOptions.value = false
    }

    // Everything for setting logging and using storage
    function logEvent(name: string, payload = null) {
        if (tracking.value)
            if (payload) {
                _logEvent(analytics, name, payload);
            } else {
                _logEvent(analytics, name);
            }
    }

    function useStorage(key: string, defaultValue: any): RemovableRef<any> | Ref<any> {
        if (storage.value) {
            return _useStorage(`${siteName}.${key}`, defaultValue)
        } else {
            return ref(defaultValue)
        }
    }

    function getFirebaseAuthPersistance() {
        if (storage.value) return browserLocalPersistence
        else return inMemoryPersistence
    }

    return { cookies, storage, tracking, showOptions, acceptAll, saveCurrent, logEvent, useStorage, getFirebaseAuthPersistance }
}
)

