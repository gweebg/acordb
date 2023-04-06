/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {

      colors: {
        text_base: "#2A303C"
      }

    }
  },
  plugins: [require("daisyui")]
};