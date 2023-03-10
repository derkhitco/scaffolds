/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
const additionalSizes = [112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320, 336]
const newSizes = {}
for (let size of additionalSizes) {
  newSizes[size] = `${size / 4}rem`
}

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: newSizes,
      colors: {
        secondary: colors.lime,
        primary: colors.cyan,
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
