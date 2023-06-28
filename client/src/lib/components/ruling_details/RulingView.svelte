<script>

    import RulingTags from "$lib/components/ruling_details/RulingTags.svelte";
    import RulingFields from "$lib/components/ruling_details/RulingFields.svelte";
    import RulingContent from "$lib/components/ruling_details/RulingContent.svelte";
    import Metadata from "$lib/components/record/Metadata.svelte";
    import Ruling from "$lib/components/ruling/Ruling.svelte";

    export let details;

    const { ruling, user } = details;
    const { added_by, added_at, acordao, tags, data } = ruling;

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

        <RulingFields fields={{fields: fields, data: data, id: acordao}} isAuthenticated={auth} isFav={details.favorite} />

        <RulingContent content={data}/>

    </div>

    <div class="mt-10">
        <h2 class="font-bold text-xl">Other Versions</h2>
        <div class="divider mt-0"></div>
        <Ruling ruling={ruling}/>

    </div>

    <div class="mt-10">
        <div class="divider"></div>
        <Metadata record={{added_by: added_by, added_at: added_at, id: acordao}}/>
    </div>

</main>

