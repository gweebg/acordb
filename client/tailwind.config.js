/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  daisyui: {
    themes: [
      {
        base: {
          'primary' : '#570df8',
          'primary-focus' : '#4506cb',
          'primary-content' : '#ffffff',

          'secondary' : '#f000b8',
          'secondary-focus' : '#bd0091',
          'secondary-content' : '#ffffff',

          'accent' : '#37cdbe',
          'accent-focus' : '#2ba69a',
          'accent-content' : '#ffffff',

          'neutral' : '#3b424e',
          'neutral-focus' : '#2a2e37',
          'neutral-content' : '#ffffff',

          'base-100' : '#ffffff',
          'base-200' : '#f9fafb',
          'base-300' : '#ced3d9',
          'base-content' : '#1e2734',

          'info' : '#1c92f2',
          'success' : '#009485',
          'warning' : '#ff9900',
          'error' : '#ff5724',
        },
      },
    ],
  },

  theme: {
    extend: {

      colors: {
        "card-accent": "#ebf3f8",
        text_base: "#2A303C"
      }

    }
  },
  plugins: [require("daisyui")]
};