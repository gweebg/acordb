<script>
    import { page } from '$app/stores';

	import SearchResults from '$lib/components/search/SearchResults.svelte';
    import SearchForm from "$lib/components/search/SearchForm.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";
    import Footer from "$lib/components/Footer.svelte";

    export let data;

    let query = {};

    $page.url.searchParams.forEach((value, key) => {

        if (key === "tags[]") {
            if (!query.tags) query["tags"] = [];
            query.tags.push(value);
        }

        else query[key] = value;

    });

    const isAuthenticated = !!data.user;

    let isAdmin = false;
    if (data.user) isAdmin = data.user.is_administrator;
    
    
</script>

<svelte:head>
    <title>
        Search
    </title>
</svelte:head>

<div class="flex flex-col h-screen">

    <!-- Navbar -->
    <Navbar isAuthenticated={isAuthenticated} isAdmin={isAdmin}/>

    <SearchForm fields={data.fields}/>

    <SearchResults query={query}/>

    <div class="mt-auto">
        <Footer/>
    </div>

</div>
