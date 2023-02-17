<template>
    <div class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5">
        <label :for="labelText" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">{{ labelText }}</label>
        <div class="mt-1 sm:col-span-2 sm:mt-0">
            <div
                class="h-12 flex items-center justify-start bg-white border border-gray-300 rounded-t-lg shadow-sm p-2">
                <button class="h-full p-1 bg-primary-700 rounded-md text-white mr-2"
                    @click="editor?.chain().focus().toggleBulletList().run()">
                    <ListBulletIcon class="h-full"></ListBulletIcon>
                </button>

                <button class="h-full p-1 bg-primary-700 rounded-l-md text-white aspect-square"
                    @click="editor?.chain().focus().toggleBold().run()">
                    <p class="font-extrabold">B</p>
                </button>
                <button class="h-full p-1 bg-primary-700 border-x border-white text-white aspect-square"
                    @click="editor?.chain().focus().toggleItalic().run()">
                    <p class="italic">I</p>
                </button>
                <button class="h-full p-1 bg-primary-700 rounded-r-md text-white aspect-square" prevendDefault
                    @click="editor?.chain().focus().toggleUnderline().run()">
                    <p class="underline">U</p>
                </button>

            </div>
            <editor-content class="bg-white rounded-b-md p-1 shadow-sm border border-gray-300" :editor="editor" />
        </div>
    </div>

</template>

<script setup lang="ts">
import { useEditor, EditorContent } from '@tiptap/vue-3'
import Document from '@tiptap/extension-document'
import Paragraph from '@tiptap/extension-paragraph'
import Bold from '@tiptap/extension-bold'
import Italic from '@tiptap/extension-italic'
import Underline from '@tiptap/extension-underline'
import Text from '@tiptap/extension-text'
import BulletList from '@tiptap/extension-bullet-list'
import ListItem from '@tiptap/extension-list-item'
import { ListBulletIcon } from '@heroicons/vue/24/outline';

const props = defineProps({
    modelValue: String,
    labelText: {
        type: String,
        required: true,
    },
})

const emits = defineEmits(['update:modelValue'])

const editor = useEditor({
    content: props.modelValue,
    onUpdate: ({ editor }) => { emits('update:modelValue', editor.getHTML()) },
    extensions: [
        Document,
        Bold.configure({ HTMLAttributes: { class: 'font-extrabold' } }),
        Italic.configure({ HTMLAttributes: { class: 'italic' } }),
        Underline.configure({ HTMLAttributes: { class: 'underline' } }),
        Paragraph.configure({ HTMLAttributes: { class: 'my-2' } }),
        Text,
        ListItem.configure({ HTMLAttributes: { class: 'ml-5' } }),
        BulletList.configure({ HTMLAttributes: { class: 'list-disc space-y-4' } }),
    ],
})

</script>