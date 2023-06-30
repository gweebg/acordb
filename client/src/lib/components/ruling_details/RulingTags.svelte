<script>

    export let tags;

    const onClick = (tag) => {
        console.log(tag);
    }

</script>

<main>

    <div class="flex flex-wrap flex-row gap-4">
        {#each tags as tag}
            <div
                on:click={() => onClick(tag)}
                class="badge badge-accent badge-lg p-4 text-white transition ease-out
                hover:-translate-y-1 hover:cursor-pointer hover:shadow-md hover:badge-neutral duration-150">
                {tag}
            </div>
        {/each}
    </div>

</main>