/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*html", "src/**/*{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        slack: {
          primary: "#350d36",
          secondary: "#3F0E40",
        },
      },
    },
  },
  plugins: [],
};
