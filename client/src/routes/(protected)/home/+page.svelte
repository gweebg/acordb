<script>

    import AdvancedSearchForm from "$lib/components/home/AdvancedSearchForm.svelte";
    import RecentlyAdded from "$lib/components/home/RecentlyAdded.svelte";

    import Statistics from "$lib/components/home/Statistics.svelte";
    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";

</script>

<div>

    <!-- Navbar -->
    <Navbar/>

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
