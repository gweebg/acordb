<script>
    import { page } from '$app/stores';
    import RecentlyAdded from "$lib/components/home/RecentlyAdded.svelte";
    import Statistics from "$lib/components/home/Statistics.svelte";
    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";
    import SearchForm from "$lib/components/search/SearchForm.svelte";

    export let data;


</script>

<svelte:head>
    <title>
        Acordb - Home
    </title>
</svelte:head>

<div>

    <!-- Navbar -->
    <Navbar isAuthenticated={data.isAuthed} isAdmin={data.isAdmin}/>

    <!-- Main content -->
    <div>

        <!-- Advanced Search -->
        <SearchForm fields={data.fields}/>
        <!-- Recently Added Rulings -->
        <RecentlyAdded/>
        <!-- Statistics -->
        <Statistics/>

    </div>

    <Footer/>
    
</div>
