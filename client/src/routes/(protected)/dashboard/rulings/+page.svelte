<script>

    import SideBar from "$lib/components/dashboard/SideBar.svelte";

</script>



<div class="flex flex-row">

    <div class="fixed">
        <SideBar active={{profile: false, rulings: true, favourites: false, settings: false, add: false}}/>
    </div>

    <!-- Content -->
    <div class="flex-1 h-screen p-12 overflow-y-auto ml-96">

        <div class="text-sm breadcrumbs">
            <ul>
                <li><p>Dashboard</p></li>
                <li><p>Your Rulings</p></li>
            </ul>
        </div>


        <h2 class="text-3xl font-bold">Your Rulings</h2>
        <div class="divider"></div>

    </div>

</div>