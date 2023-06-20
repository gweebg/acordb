<script>


    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";
    import RecordDetails from "$lib/components/record/RecordDetails.svelte";
    export let data;

    const isAuthenticated = !!data.user;

</script>

<div>

    <!-- Navbar -->
    <Navbar isAuthenticated={isAuthenticated}/>

    <!-- Main content -->
    <div>
        <RecordDetails data={data}/>
    </div>

    <Footer/>
    
</div>
