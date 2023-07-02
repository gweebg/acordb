<script>

    import RulingTags from "$lib/components/ruling_details/RulingTags.svelte";
    import RulingFields from "$lib/components/ruling_details/RulingFields.svelte";
    import RulingContent from "$lib/components/ruling_details/RulingContent.svelte";
    import Metadata from "$lib/components/record/Metadata.svelte";
    import Ruling from "$lib/components/ruling/Ruling.svelte";

    export let details;
    export let isRecord;


    const { ruling, user } = details;
    const { added_by, added_at, acordao, tags, data } = ruling;

    let versions = [];
    if (!isRecord) {
        versions = details.versions;
    }

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

        <RulingFields fields={{fields: fields, data: data, id: acordao}} isAuthenticated={auth} isFav={details.favorite} {isRecord}/>

        <RulingContent content={data}/>

    </div>

    {#if !isRecord}

        <div class="mt-10">
            <h2 class="font-bold text-xl">Outras Versões</h2>
            <div class="divider mt-0"></div>

            {#if versions.length > 0}

                {#each versions as ruling}
                    <Ruling ruling={ruling} isRecord={true}/>
                {/each}

            {:else}

                <p>Não existem outras versões para este acórdão.</p>

            {/if}
        </div>

    {/if}

    <div class="mt-10">
        <div class="divider"></div>
        <Metadata record={{added_by: added_by, added_at: added_at, id: acordao}}/>
    </div>

</main>

