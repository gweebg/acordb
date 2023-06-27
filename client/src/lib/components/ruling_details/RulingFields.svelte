<script>

    import {capitalize} from "$lib/scripts/utils.js";

    export let fields;
    export let isAuthenticated;

</script>


<div class="w-1/4 p-2 sticky top-24 h-full">

    <p class="text-xl font-bold">Process no. {fields.data.Processo}</p>
    <div class="divider m-0"></div>

    {#each fields.fields as field}
        <div class="mb-1">
            <p class="text-neutral">{capitalize(field)}</p>
            <p class="opacity-70">{fields.data[field]}</p>
        </div>
    {/each}

    <div class="mt-4 flex flex-row flex-wrap gap-2">

        <a href={"http://www.dgsi.pt/" + fields.data.url} target="_blank" class="btn btn-sm">DGSI</a>

        <!-- TODO Dar funções aos botões e meter icons :) -->
        {#if isAuthenticated}
            <button class="btn btn-sm">Bookmark</button>
            <button class="btn btn-sm">Suggest Change</button>
        {/if}

    </div>

</div>

