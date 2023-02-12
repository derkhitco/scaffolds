<template>
    <Notifcation 
    :mode="message.mode" 
    :open="message.show" 
    :message="message.message" 
    :title="message.title"
    @close="message.show = false" ></Notifcation>
    <div class="px-4 sm:px-6 lg:px-8">
        <div class="sm:flex sm:items-center">
            <div class="sm:flex-auto">
                <h1 class="admin-title-1">{%PAGETEXTCAPITAL%} pagina</h1>
                <p class="admin-text-1">Hier kan je de {%PAGETEXT%} pagina bewerken.</p>
            </div>
        </div>

        <div class="space-y-6 sm:space-y-5">
            <StringInput v-model="pageStore.{%PAGESTORE%}.title" label-text="Titel" />
        </div>

        <div class="flex justify-end my-3">
            <button type="submit" @click="save" class="btn-primary-1">Opslaan</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import Notifcation from '../../components/alerts/Notification.vue';
import StringInput from '../../components/inputs/StringInput.vue';
import { usePageStore } from '../../stores/pages';
import { ref } from 'vue';

const pageStore = usePageStore();
const message = ref({show: false, mode: 'success', title: 'Gelukt!', message: 'Je wijzigingen zijn opgeslagen'});

function save() {
    pageStore.save().then(() => {
        message.value = {show: true, mode: 'success', title: 'Gelukt!', message: 'Je wijzigingen zijn opgeslagen.'}
    }).catch(() => {
        message.value = {show: true, mode: 'error', title: 'Fout!', message: 'Er is iets fout gegaan.'}
    })
}

</script>

