<script>

    import RequestsIn from "$lib/components/dashboard/RequestsIn.svelte";
    import SideBar from "$lib/components/dashboard/SideBar.svelte";

    export let data;

</script>

<svelte:head>
    <title>
        Acordb - Pedidos de Revisão
    </title>
</svelte:head>

<div class="flex flex-row">

    <div class="fixed">
        <SideBar
                active={{profile: false, rulings: false, favourites: false, settings: false, requests: true}}
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
                    <li><p>Pedidos de Revisão</p></li>
                </ul>
            </div>

            {#if data.user.is_administrator}
                <h2 class="text-3xl font-bold">Pedidos de Revisão Recebidos</h2>
            {:else}
                <h2 class="text-3xl font-bold">Pedidos de Revisão Enviados</h2>
            {/if}
            <div class="divider"></div>

        </header>

        <!-- Content -->
        <div class="flex flex-col">

            <RequestsIn requests={data.data} isAdmin={data.user.is_administrator}/>

        </div>


    </div>
</div>