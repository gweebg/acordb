<script>
    import { page } from '$app/stores';
    import Footer from "$lib/components/Footer.svelte";
	import AdvancedSearchForm from '$lib/components/home/AdvancedSearchForm.svelte';
    import Navbar from "$lib/components/home/Navbar.svelte";
	import SearchResults from '$lib/components/search/searchResults.svelte';

    export let data;

    let query = {};

    page.subscribe((value) => {
        for (const key of value.url.searchParams.keys()) {
            query[key] = value.url.searchParams.get(key);
        }
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

<div>

    <!-- Navbar -->
    <Navbar isAuthenticated={isAuthenticated} isAdmin={isAdmin}/>

    <AdvancedSearchForm/>

    <SearchResults query={query}/>

    <Footer/>
    
</div>
