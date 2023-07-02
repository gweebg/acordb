<script>

    import RequestItem from "$lib/components/dashboard/RequestItem.svelte";

    export let requests;
    export let isAdmin;

</script>


<main class="flex gap-4 flex-col">

    {#if requests.length === 0}

        <h2 class="text-xl flex justify-center">Experimenta fazer um pedido de revisão!</h2>

    {:else}
        {#each requests as req (req.id)}

            <RequestItem details={req} {isAdmin}/>

        {/each}
    {/if}

</main>

