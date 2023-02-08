<template>
    <div class="relative bg-primary-800">
        Hier kunnen dingen geplaats worden
        <img :src="textStore.home?.image?.url" alt="">
        <h1>{{textStore.home?.title}}</h1>
        <p>{{textStore.home?.description}}</p>
    </div>
</template>

<script setup lang="ts">
import { useTextStore } from '../stores/texts'
const textStore = useTextStore()

</script>