<script>

    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";
    import RulingView from "$lib/components/ruling_details/RulingView.svelte";

    export let data;

    const isAuthenticated = !!data.user;

    let isAdmin = false;
    if (data.user) isAdmin = data.user.is_administrator;

</script>

<svelte:head>
    <title>
        Ruling {data.ruling.data.Processo}
    </title>
</svelte:head>

<div>

    <!-- Navbar -->
    <Navbar isAuthenticated={isAuthenticated} isAdmin={isAdmin}/>

    <!-- Main content -->
    <div>
        <RulingView details={data}/>
    </div>

    <Footer/>
    
</div>
