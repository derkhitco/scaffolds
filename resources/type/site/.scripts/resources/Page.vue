<template>
    <div class="relative bg-white">
        <h1 class="text-primary-600 text-3xl text-center">{{ pageStore.{%PAGESTORE%}.title }}</h1>
    </div>
</template>

<script setup lang="ts">
import { usePageStore } from '../../stores/pages'
const pageStore = usePageStore()

</script>