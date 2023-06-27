<script>

    export let rulingData;

</script>

<main>

    <section>
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


    <section class="flex flex-row gap-2 flex-wrap mb-2">
        {#each rulingData.descriptors as d}
            <div class="badge badge-neutral badge-lg">{d}</div>
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