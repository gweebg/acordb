<script>

    import { Toaster } from "svelte-french-toast";

    import { capitalize } from "$lib/scripts/utils.js";
    import FavoriteButton from "$lib/components/FavoriteButton.svelte";
    import SuggestButton from "$lib/components/sugestion/SuggestButton.svelte";

    export let fields;
    export let isAuthenticated;
    export let isFav;
    export let isRecord;

</script>

<Toaster/>

<div class="w-1/4 p-2 sticky top-24 h-full">

    <p class="text-xl font-bold">Process no. {fields.data.Processo}</p>
    <div class="divider m-0"></div>

    {#each fields.fields as field}
        <div class="mb-1">
            <p class="text-neutral font-semibold">{capitalize(field)}</p>
            <p class="opacity-70 break-words">{fields.data[field]}</p>
        </div>
    {/each}

    <div class="mt-4 flex flex-row flex-wrap gap-2">

        <a href={"http://www.dgsi.pt/" + fields.data.url} target="_blank" class="btn btn-sm">Open in DGSI</a>

        {#if isAuthenticated && !isRecord}

            <FavoriteButton id={fields.id} isDisabled={isFav}>

                <button class="btn btn-sm" disabled={isFav}>Save in Favorites</button>

            </FavoriteButton>

            <SuggestButton ruling={fields.data} id={fields.id}>

                <button class="btn btn-sm">Suggest a Change</button>

            </SuggestButton>

        {/if}

    </div>

</div>

