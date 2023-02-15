<template>
    <div class="bg-secondary border border-gray-200 p-2 m-2 flex items-center flex-col">
        <button class="bg-gray-200 rounded-md text-black px-2 py-1 text-sm mb-3"
            @click="emits('remove')">verwijder</button>
        <img class="w-16" :src="img?.url" alt="">
    </div>
</template>

<script setup lang="ts">
import {PropType} from 'vue'
import { FileObject } from './../../util/types'
const emits = defineEmits(['remove'])
const props = defineProps({ img: {type: Object as PropType<FileObject>} })
</script>