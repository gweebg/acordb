import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: "0.0.0.0",
		hmr: {
		  clientPort: 80,
		},
		port: 80, 
		watch: {
		  usePolling: true,
		},
	  }
});
