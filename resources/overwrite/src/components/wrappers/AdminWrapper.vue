<template>
  <div>
    <TransitionRoot as="template" :show="sidebarOpen">
      <Dialog as="div" class="relative z-40 md:hidden" @close="sidebarOpen = false">
        <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0"
          enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100"
          leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
        </TransitionChild>

        <div class="fixed inset-0 z-40 flex">
          <TransitionChild as="template" enter="transition ease-in-out duration-300 transform"
            enter-from="-translate-x-full" enter-to="translate-x-0"
            leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0"
            leave-to="-translate-x-full">
            <DialogPanel class="relative flex w-full max-w-xs flex-1 flex-col bg-primary-700 pt-5 pb-4">
              <TransitionChild as="template" enter="ease-in-out duration-300" enter-from="opacity-0"
                enter-to="opacity-100" leave="ease-in-out duration-300" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 right-0 -mr-12 pt-2">
                  <button type="button"
                    class="ml-1 flex h-10 w-10 items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                    @click="sidebarOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <XMarkIcon class="h-6 w-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>
              <div class="flex flex-shrink-0 items-center px-4 justify-center">
                <LogoComponent class="h-16"></LogoComponent>
              </div>
              <div class="mt-5 h-0 flex-1 overflow-y-auto">
                <nav class="space-y-1 px-2">
                  <RouterLink v-for="item in navigation" @click="current = item.name" :key="item.name" :to="item.href"
                    :class="[item.name == current ? 'bg-primary-800 text-white' : 'text-primary-100 hover:bg-primary-600', 'group flex items-center px-2 py-2 text-base font-medium rounded-md']">
                    <component :is="getIcon(item.name)" class="mr-4 h-6 w-6 flex-shrink-0 text-primary-300"
                      aria-hidden="true" />
                    {{ item.name }}
                  </RouterLink>
                </nav>
              </div>
            </DialogPanel>
          </TransitionChild>
          <div class="w-14 flex-shrink-0" aria-hidden="true">
            <!-- Dummy element to force sidebar to shrink to fit close icon -->
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Static sidebar for desktop -->
    <div class="hidden md:fixed md:inset-y-0 md:flex md:w-64 md:flex-col">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="flex flex-grow flex-col overflow-y-auto bg-primary-700 pt-5">
        <div class="flex flex-shrink-0 items-center px-4 justify-center">
          <LogoComponent class="h-16"></LogoComponent>
        </div>
        <div class="mt-5 flex flex-1 flex-col">
          <nav class="flex-1 space-y-1 px-2 pb-4">
            <RouterLink v-for="item in navigation" :key="item?.name" :to="item.href"
              @click="current = item.name"
              :class="[item.name == current ? 'bg-primary-800 text-white' : 'text-primary-100 hover:bg-primary-600', 'group flex items-center px-2 py-2 text-sm font-medium rounded-md']">
              <component :is="getIcon(item.name)" class="mr-3 h-6 w-6 flex-shrink-0 text-primary-300"
                aria-hidden="true" />
              {{ item.name }}
            </RouterLink>
          </nav>
        </div>
      </div>
    </div>
    <div class="flex flex-1 flex-col md:pl-64">
      <div class="sticky top-0 z-10 flex h-16 flex-shrink-0 bg-white shadow">
        <button type="button"
          class="border-r border-gray-200 px-4 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-primary-500 md:hidden"
          @click="sidebarOpen = true">
          <span class="sr-only">Open sidebar</span>
          <Bars3BottomLeftIcon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>

      <main class="h-full">
        <div class="py-6">
          <div class="mx-auto h-full max-w-7xl px-4 sm:px-6 md:px-8">
            <RouterView />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import LogoComponent from '../../components/misc/LogoComponent.vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { Bars3BottomLeftIcon, DocumentTextIcon, XMarkIcon } from '@heroicons/vue/24/outline'
import { useRouter } from 'vue-router';

const current = ref('index')

function getIcon(name: string) {
  switch (name) {
    case 'hometexts':
      return DocumentTextIcon
    default:
      return DocumentTextIcon
  }
}


const navigation = computed((): { name: string, href: string }[] => {
  const children = router.getRoutes().filter((route) => route.path == '/admin/' && route.children.length > 0)[0].children
  const results = children.map((child) => {
    if (child.meta?.inHeader) {
      return {
        name: child.name?.toString(),
        href: '/admin/' + child.path.toString(),
      }
    }
  }).filter((item): item is { name: string, href: string } => item !== undefined)
  return results
})

const navigation2 = [
  { name: 'home', href: '/admin/hometexts', icon: DocumentTextIcon, current: false }
]


const router = useRouter();

const sidebarOpen = ref(false)
</script>