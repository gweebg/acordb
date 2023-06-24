<script>

    import AdvancedSearchForm from "$lib/components/home/AdvancedSearchForm.svelte";
    import RecentlyAdded from "$lib/components/home/RecentlyAdded.svelte";
    import Statistics from "$lib/components/home/Statistics.svelte";
    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";

    export let data;

</script>

<div>

    <!-- Navbar -->
    <Navbar isAuthenticated={data.isAuthed} isAdmin={data.isAdmin}/>

    <!-- Main content -->
    <div>

        <!-- Advanced Search -->
        <AdvancedSearchForm/>
        <!-- Recently Added Rulings -->
        <RecentlyAdded/>
        <!-- Statistics -->
        <Statistics/>

    </div>

    <Footer/>
    
</div>
