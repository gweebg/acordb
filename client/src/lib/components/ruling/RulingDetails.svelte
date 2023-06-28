<script>

    export let rulingData;

</script>

<main>

    <section class="mt-2">
        <p class="text-lg mb-1">
            <span class="font-bold">Court House:</span>
            {rulingData.court}
        </p>

        <p class="text-lg mb-1">
            <span class="font-bold">Rapporteur:</span>
            {rulingData.rapporteur}
        </p>

        <p class="text-lg mb-2">
            <span class="font-bold">Ruling Date:</span>
            {rulingData.ruling_date}
        </p>
    </section>


    <section class="flex flex-row gap-2 flex-wrap my-4">
        {#each rulingData.descriptors as d}
            <div class="badge badge-accent badge-lg text-white">{d}</div>
        {/each}
    </section>

    <div class="divider my-0"></div>

    <section class="text-lg mb-2">
        <p class="truncate nowrap overflow-hidden">

            {#if rulingData.text}
                {rulingData.text}
            {/if}

        </p>
    </section>

</main>