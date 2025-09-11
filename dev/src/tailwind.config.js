/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Add paths to all your Django templates
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    // Add paths to JS files if using Tailwind classes in JavaScript
    "./static/src/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

