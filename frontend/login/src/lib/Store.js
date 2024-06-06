import { writable } from 'svelte/store';

const ThemeStore = writable(
  {
    theme: localStorage.getItem("color-theme") || 'dark',
  },
);

export default ThemeStore;