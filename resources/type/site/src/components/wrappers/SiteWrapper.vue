<template>
    <HeaderBar></HeaderBar>
    <RouterView/>
    <FooterBar></FooterBar>
</template>

<script setup lang="ts">
import HeaderBar from '../home/HeaderBar.vue';
import FooterBar from '../home/FooterBar.vue';
import { useRouter } from 'vue-router';
const router = useRouter();
</script>