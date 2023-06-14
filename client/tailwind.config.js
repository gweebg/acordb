/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  daisyui: {
    themes: [
      {
        base: {
          "primary": "#ea60be",
          "secondary": "#bfbdfc",
          "accent": "#2dbcab",
          "neutral": "#202131",
          "base-100": "#e4e9ec",
          "info": "#3da9db",
          "success": "#2abb9e",
          "warning": "#faab57",
          "error": "#f85474",
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