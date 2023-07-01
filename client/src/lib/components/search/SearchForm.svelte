<script>

    import SearchFormHeader from "$lib/components/search/SearchFormHeader.svelte";
    import SearchFormBody from "$lib/components/search/SearchFormBody.svelte";

    export let fields;

</script>


<main class="px-4 mb-[100px] mt-[80px] mx-48">

    <SearchFormHeader/>

    <SearchFormBody {fields}/>

</main>