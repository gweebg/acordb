<script>

    import RulingContentSection from "$lib/components/ruling_details/RulingContentSection.svelte";

    export let content;

</script>


<main class="p-2 w-3/4">

    <RulingContentSection field={"Sumário"} value={content["Sumário"]}/>
    <RulingContentSection field={"Texto Integral"} value={content["Texto Integral"]}/>
    <RulingContentSection field={"Decisão"} value={content["Decisão"]}/>

</main>