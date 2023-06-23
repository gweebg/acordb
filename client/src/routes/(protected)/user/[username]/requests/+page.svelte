<script>

    import RequestsIn from "$lib/components/dashboard/RequestsIn.svelte";
    import SideBar from "$lib/components/dashboard/SideBar.svelte";

    export let data;

</script>


<div class="flex flex-row">

    <div class="fixed">
        <SideBar
                active={{profile: false, rulings: true, favourites: false, settings: false, add: false}}
                name={data.user.email}
                basePath={"/user/" + data.user.id}
                isAdmin={data.user.is_administrator}
        />
    </div>

    <!-- Content -->
    <div class="flex-1 h-screen p-12 overflow-y-auto ml-96">

        <!-- Header -->
        <header>

            <div class="text-sm breadcrumbs">
                <ul>
                    <li><p>Dashboard</p></li>
                    <li><p>Incoming Change Requests</p></li>
                </ul>
            </div>


            <h2 class="text-3xl font-bold">Incoming Change Requests</h2>
            <div class="divider"></div>

        </header>

        <!-- Content -->
        <div class="flex flex-col">

            <RequestsIn requests=""/>

        </div>


    </div>
</div>