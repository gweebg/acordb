import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import basicSsl from '@vitejs/plugin-basic-ssl'



export default defineConfig({
	server: {
		host: "0.0.0.0",
		hmr: {
		  clientPort: 80,
		},
		port: 80, 
		watch: {
		  usePolling: true,
		},
		// https: true
	},
	plugins: [sveltekit()],
	ssr: {
        noExternal: ['sveltekit-flash-message', '@auth/sveltekit', '@vitejs/plugin-basic-ssl'],
    },
});
