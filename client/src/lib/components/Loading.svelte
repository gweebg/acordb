<script>

    import { loading } from "$lib/stores/loading.js";
    import { slide } from 'svelte/transition';

</script>

{#if $loading}

    <div class="bg-accent flex justify-center p-1" transition:slide>
        <span class="loading loading-dots loading-md"></span>
    </div>

{/if}


