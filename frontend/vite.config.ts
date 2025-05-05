// import { defineConfig } from 'vite';
import { defineConfig } from 'vitest/config';
import vue from '@vitejs/plugin-vue';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
  },
  test: {
    environment: 'jsdom',
    globals: true,
  },
});
