<template>
    <div class="max-w-7xl m-auto">
        <header class="h-20 sticky flex flex-row items-center justify-between z-20 w-full px-10">
            <NuxtLink to="/">
                <LogoComponent class="py-2 h-16"></LogoComponent>
            </NuxtLink>

            <div class="">
                <!-- dummy div to push the router links in the center -->
            </div>
        </header>
    </div>
</template>

<script setup lang="ts">
const router = useRouter()

const navigation = computed((): { name: string, href: string }[] => {
        
    
    const children = router.getRoutes().filter((route) => route.path == '/' && route.children.length > 0)[0].children
    const results = children.map((child) => {
        if (child.meta?.inHeader) {
            return {
                name: child.name?.toString(),
                href: child.path.toString(),
            }
        }
    }).filter((item): item is { name: string, href: string } => item !== undefined)
    return results
})

</script>