/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./layouts/**/*.html",
    "./content/**/*.md",
    "./safelist.txt"
  ],
  theme: {
    extend: {
      screens: {
        '3xl': '1920px',
      },
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
      boxShadow: {
        DEFAULT: '0px 0px 2px rgba(21, 21, 21, 0.14), 0px 2px 4px rgba(21, 21, 21, 0.16)',
        md: '0px 1px 2px rgba(21, 21, 21, 0.1), 0px 3px 7px rgba(21, 21, 21, 0.1), 0px 12px 30px rgba(21, 21, 21, 0.08)',
        lg: '0px 4px 10px rgba(21, 21, 21, 0.1), 0px 12px 30px rgba(21, 21, 21, 0.17)',
      },
      typography: {
        DEFAULT: {
            css: {
              fontWeight: '400',
              'h2': {
                fontWeight: '600',
              },
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
