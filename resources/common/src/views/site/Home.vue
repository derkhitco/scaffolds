<template>

    <div class="relative h-full bg-primary-800">
        Hier kunnen dingen geplaats worden
        <img :src="pageStore.home?.image?.url" alt="">
        <h1>{{ pageStore.home?.title }}</h1>
        <p>{{ pageStore.home?.description }}</p>
    </div>
</template>

<script setup lang="ts">
import { usePageStore } from '../../stores/pages'
const pageStore = usePageStore()

</script>