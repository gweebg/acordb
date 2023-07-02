/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  daisyui: {
    themes: [
      {
        base: {
          'primary' : '#f9d72f',
           'primary-focus' : '#e9c307',
           'primary-content' : '#18182f',

           'secondary' : '#be8b1e',
           'secondary-focus' : '#a87b1a',
           'secondary-content' : '#ffffff',

           'accent' : '#18182f',
           'accent-focus' : '#111122',
           'accent-content' : '#ffffff',

           'neutral' : '#18182f',
           'neutral-focus' : '#111122',
           'neutral-content' : '#ffffff',

           'base-100' : '#ffffff',
           'base-200' : '#f5f5f5',
           'base-300' : '#e3e3e3',
           'base-content' : '#000000',

           'info' : '#4A90E2',
           'success' : '#82DD55',
           'warning' : '#EDB95E',
           'error' : '#E23636',
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