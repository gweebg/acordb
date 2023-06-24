<script>

    import {loading} from "$lib/stores/loading.js";

</script>

{#if $loading}

    <div class="bg-accent flex justify-center p-1">

        <span class="loading loading-dots loading-md"></span>
<!--        <span class="loading loading-infinity loading-md"></span>-->
    </div>

{/if}


