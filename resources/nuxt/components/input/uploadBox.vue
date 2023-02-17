<template>
    <div class="space-y-1 text-center">
        <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48"
            aria-hidden="true">
            <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <label :for="id"
            class="relative cursor-pointer rounded-md bg-white font-medium text-primary-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-primary-500 focus-within:ring-offset-2 hover:text-primary-500">
            <span>{{ text }}</span>
            <input :id="id" :name="id" type="file" class="sr-only" @change="upload" />
        </label>
    </div>
</template>

<script setup lang="ts">
import { v4 as uuidv4 } from 'uuid';

const props = defineProps({ text: String, types: { type: Array<String>, required: true} });
const emits = defineEmits(['file']);
const id = `file-upload-${uuidv4()}`;

function upload(e: Event) {
    const target: HTMLInputElement = e.target as HTMLInputElement
    const files: FileList = target.files as FileList
    if (props.types?.length > 0){
        if (!props.types.includes(files[0].type)) {
            alert('Dit bestandstype is niet toegestaan')
            return
        }
    }
    const img = files[0]
    const imgUrl = URL.createObjectURL(img)
    emits('file', { url: imgUrl, file: img })
}


</script>