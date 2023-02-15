<template>
    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
        <label :for="labelText" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">{{ labelText }}</label>
        <div class="mt-1 sm:col-span-2 sm:mt-0">
            <div class="flex max-w-lg rounded-md shadow-sm">
                <textarea v-model="value" type="text" :name="labelText" :id="labelText" :rows="rows || 3"
                    class="block w-full min-w-0 flex-1 rounded-md border-gray-300 focus:border-primary-500 focus:ring-primary-500 sm:text-sm" />
            </div>
        </div>
    </div>
</template>


<script setup lang="ts">
import { computed } from 'vue';
const props = defineProps({ modelValue: String, labelText: String, rows: { type: Number, required: false } });
const emit = defineEmits(['update:modelValue']);
const value = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
});

</script>