/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./layouts/**/*.html",
    "./content/**/*.md",
    "./safelist.txt"
  ],
  theme: {
    extend: {
      // These are for @container queries specifically
      containers: {
        'nip': '10rem',
        'short': '15rem',
        'tall': '20rem',
        'grande': '30rem',
        'venti': '40rem',
        'trenta': '50rem',
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
