<template>
    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
        <label :for="labelText" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">{{ labelText }}</label>
        <div class="mt-1 sm:col-span-2 sm:mt-0">
            <div class="w-full rounded-md border-dashed border-2 border-gray-300 p-6">
                <uploadBox v-if="!modelValue" :types="types"
                    :text="`Klik hier om ${imageName ? imageName : ''} te uploaden`" @file="addImage"></uploadBox>
                <PresentImageCard v-if="modelValue" :img="modelValue" @remove="removeImage"></PresentImageCard>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { PropType } from 'vue'
import { FileObject } from './../../util/types'
import PresentImageCard from './PresentImageCard.vue';
import uploadBox from './uploadBox.vue';

const props = defineProps({
    modelValue: { type: Object as PropType<FileObject> },
    imageName: String,
    labelText: String,
    types: { type: Array<String>, default: () => ['image/svg+xml', 'image/jpeg', 'image/png', 'image/x-icon', 'image/apng', 'image/avif'] }
})
const emits = defineEmits(['update:modelValue'])

function addImage(img: FileObject) {
    emits('update:modelValue', img)
}

function removeImage() {
    emits('update:modelValue', undefined)
}

</script>


