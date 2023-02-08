<template>
    <div class="px-4 sm:px-6 lg:px-8">
        <div class="sm:flex sm:items-center">
            <div class="sm:flex-auto">
                <h1 class="text-xl font-semibold text-gray-900">Home page texts</h1>
                <p class="mt-2 text-sm text-gray-700">All texts for on your homepage</p>
            </div>
        </div>

        <div class="space-y-6 sm:space-y-5">
            <StringInput v-model="home.title" label-text="Title" />
            <ImageUpload v-model="home.image" label-text="Background picture" />
            <RichTextInput v-model="home.description" label-text="Description" />
        </div>

        <div class="flex justify-end my-3">
            <button type="submit" @click="textStore.save()"
                class="ml-3 inline-flex justify-center rounded-md border border-transparent bg-primary-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2">Opslaan</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import ImageUpload from '../../components/inputs/ImageUpload.vue';
import StringInput from '../../components/inputs/StringInput.vue';
import RichTextInput from '../../components/inputs/RichTextInput.vue';
import { useTextStore } from '../../stores/texts';
import { computed } from 'vue';
import { HomeTexts } from '../../util/types';

const textStore = useTextStore();
const home = computed({
    get() {
        if (textStore.home) {
            return textStore.home
        } else {
            return { title: '' } as HomeTexts
        }
    },
    set(value: HomeTexts) {
        textStore.home = value
    }
})

</script>

