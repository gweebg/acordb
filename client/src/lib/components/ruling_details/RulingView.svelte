<script>

    import RulingTags from "$lib/components/ruling_details/RulingTags.svelte";
    import RulingFields from "$lib/components/ruling_details/RulingFields.svelte";
    import RulingContent from "$lib/components/ruling_details/RulingContent.svelte";
    import {capitalize} from "$lib/scripts/utils.js";

    export let details;

    const { ruling, user } = details;

    const { added_by, added_at, tags, data } = ruling;

    let fields = Object.keys(data);
    fields = fields.filter((field) => {
        const toRemove = ["Texto Integral", "url", "Texto das Cláusulas Abusivas", "Sumário", "Decisão"];
        return !toRemove.includes(field);
    })

    const auth = user !== null;

</script>


<main class="px-4 mb-[100px] mt-[80px] mx-48">

    <RulingTags tags={tags}/>

    <div class="flex gap-6 mt-4">

<!--        <RulingFields fields={{fields: fields, data: data}} isAuthenticated={auth}/>-->

        <div class="w-1/4 p-2 sticky top-24 h-full">

            <p class="text-xl font-bold">Process no. {data.Processo}</p>
            <div class="divider m-0"></div>

            {#each fields as field}
                <div class="mb-1">
                    <p class="text-neutral">{capitalize(field)}</p>
                    <p class="opacity-70">{data[field]}</p>
                </div>
            {/each}

            <div class="mt-4 flex flex-row flex-wrap gap-2">

                <a href={"http://www.dgsi.pt/" + data.url} target="_blank" class="btn btn-sm">DGSI</a>

                <!-- TODO Dar funções aos botões e meter icons :) -->
                {#if auth}
                    <button class="btn btn-sm">Bookmark</button>
                    <button class="btn btn-sm">Suggest Change</button>
                {/if}

            </div>

        </div>

        <RulingContent content={data}/>

    </div>

</main>

