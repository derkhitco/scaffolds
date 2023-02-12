if [ -z $1 ] 
then
  echo "Please provide a project name"
  exit 1
else
    # Initiate the project
    echo "Creating a new project called $1"
    yarn create vite $1 --template vue-ts

    # Install dependencies
    cd $1
    yarn install
    yarn add -D tailwindcss postcss autoprefixer
    yarn add vite-ssr vue@3 vue-router@4 @vueuse/head @headlessui/vue @heroicons/vue @tiptap/core @tiptap/extension-underline @tiptap/pm @tiptap/starter-kit @tiptap/vue-3 firebase pinia uuid vue-heroicons @vueuse/core @tailwindcss/forms
    npx tailwindcss init -p

    # Copy the resources folder
    cd -
    rm -rf $1/src/components $1/src/assets $1/src/components
    cp -rf resources/overwrite/*  ./$1
    touch ./$1/src/.gitignore
    echo "scripts" >> ./$1/src/.gitignore
    python3 ./scripts.py ./$1/package.json
fi