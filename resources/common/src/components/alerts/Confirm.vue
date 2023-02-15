<template>
    <ModalWrapper :open="open" bg-color="bg-white" :bg-close="true" @close="emits('cancel')">
        <div class="rounded-md p-4">
            <div class="flex">
                <div class="flex-shrink-0">
                    <ExclamationTriangleIcon class="h-5 w-5 text-yellow-400" aria-hidden="true" />
                </div>
                <div class="ml-3">
                    <h3 class="text-sm font-medium ">{{ title }}</h3>
                    <div class="mt-2 text-sm">
                        <p>{{ message }}</p>
                    </div>
                    <div class="flex flex-row space-x-3 pt-4 justify-end">
                        <button @click="emits('cancel')"
                            class="inline-flex items-center rounded-md border border-transparent bg-yellow-100 px-4 py-2 text-sm font-medium text-yellow-800 hover:bg-yellow-200 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:ring-offset-2">
                            {{ cancelText }}</button>
                        <button @click="emits('confirm')"
                            class="inline-flex items-center rounded-md border border-transparent bg-yellow-300 px-4 py-2 text-sm font-medium text-yellow-800 hover:bg-yellow-400 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:ring-offset-2">
                            {{ confirmText }}</button>
                    </div>
                </div>
            </div>
        </div>
    </ModalWrapper>
</template>


<script setup lang="ts">
import ModalWrapper from '../misc/ModalWrapper.vue';
import { ExclamationTriangleIcon } from '@heroicons/vue/20/solid'
const props = defineProps({
    open: {
        type: Boolean,
        required: true
    },
    title: String,
    message: String,
    confirmText: { type: String, default: 'Doorgaan' },
    cancelText: { type: String, default: 'Annuleren' }
})

const emits = defineEmits(['cancel', 'confirm'])

</script>