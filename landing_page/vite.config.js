import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,       // you can change the port if you want
    open: true        // opens browser automatically on server start
  },
  build: {
    outDir: 'dist'    // default output folder for build
  }
});
