/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./themes/**/layouts/**/*.html",
    "./layouts/**/*.html",
    "./content/**/*.md",
    "./data/cards.yaml",
    "./safelist.txt"
  ],
  theme: {
    extend: {
      // These are for @container queries specifically
      containers: {
        'tall': '10rem',
        'grande': '20rem',
        'venti': '40rem',
      },
      fontFamily: {
        sans: ['"Open Sans"', 'sans-serif'],
        mono: ['"Source Code Pro"', 'monospace'],
      },
      typography: {
        DEFAULT: {
            css: {
              fontWeight: '400',
              'a': {
                fontWeight: '400',
              },
            },
          },
        quoteless: {
          css: {
            'blockquote p:first-of-type::before': { content: 'none' },
            'blockquote p:first-of-type::after': { content: 'none' },
            'code::before': { content: 'none' },
            'code::after': { content: 'none' },
            '> ul > li > input:first-child': {
              marginTop: 0,
            },
            '> ul > li > input:last-child': {
              marginBottom: 0,
            },
            '> ol > li > input:first-child': {
              marginTop: 0,
            },
            '> ol > li > input:last-child': {
              marginBottom: 0,
            },
            '.gist .highlight tbody tr': {
              borderWidth: 0,
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
