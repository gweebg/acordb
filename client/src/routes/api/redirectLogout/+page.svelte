<script>
	import { browser } from '$app/environment';
// ...Your other imports

if (browser) { // to prevent error window is not defined, because it's SSR
    window.location.href = 'http://localhost/login';
}
</script>