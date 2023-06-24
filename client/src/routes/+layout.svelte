<script>
    import '../app.scss';

    import {navigating} from "$app/stores";
    import {loading} from "$lib/stores/loading.js";

    import Loading from "$lib/components/Loading.svelte";

    $: $loading = !!$navigating
</script>

<Loading/>

<slot/>

