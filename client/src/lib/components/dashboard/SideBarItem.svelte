<script>

    export let params;

</script>


<a
    class="btn gap-4 text-left justify-start items-center text-base-100-focus {params.isActive ? 'btn-accent' : ''}"
    href={params.link}>

    {#if params.isActive}
        <img class="dark-icon" src={params.iconPath} alt={params.text}>

    {:else}
        <img src={params.iconPath} alt={params.text}>

    {/if}

    {params.text}

</a>

<style>

    .dark-icon {
        filter: brightness(15%);
    }

</style>
