<template>
    <NuxtLayout>
        <div class="bg-primary-200 text-black text-center m-auto p-auto">
            The basis pagina {{ pageStore.home.title }}
        </div>
    </NuxtLayout>
</template>

<script setup lang="ts">
import { useUserStore } from '~/stores/users';
import { usePageStore } from '~/stores/pages'

definePageMeta({ auth: true, title: 'Home'})

const pageStore = usePageStore()

</script>