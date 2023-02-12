<template>
    <div class="max-w-7xl m-auto">
        <header class="h-20 sticky flex flex-row items-center justify-between z-20 w-full px-10">
            <RouterLink to="/">
                <LogoComponent class="py-2 h-16"></LogoComponent>
            </RouterLink>
            <div>
                <RouterLink v-for="item in navigation" :key="item.name" :to="item.href">{{ item.name }}</RouterLink>
            </div>
            <div class="">
                <!-- dummy div to push the router links in the center -->
            </div>
        </header>
    </div>
</template>

<script setup lang="ts">
import LogoComponent from './../misc/LogoComponent.vue'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const navigation = computed((): { name: string, href: string }[] => {
    const children = router.getRoutes().filter((route) => route.path == '/' && route.children.length > 0)[0].children
    const results = children.map((child) => {
        if (child.meta?.inHeader) {
            console.log(child)
            return {
                name: child.name?.toString(),
                href: child.path.toString(),
            }
        }
    }).filter((item): item is { name: string, href: string } => item !== undefined)
    return results
})

</script>