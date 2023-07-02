<script>

    // export let isAuth;
    import NavbarAuthSection from "$lib/components/home/NavbarAuthSection.svelte";
    import NavbarNoAuthSection from "$lib/components/home/NavbarNoAuthSection.svelte";

    let windowY;

    export let isAuthenticated;
    export let isAdmin;

</script>

<svelte:window bind:scrollY={windowY}/>

<div class="bg-base-100 sticky top-0 z-50 {windowY > 1 ? 'navbar-shadow' : 'navbar-shadow-out'}">

    <header id="navbar" class="header-area mx-48">

        <!-- Navbar -->
        <div class="navbar border-none px-4">

            <!-- Left Items -->
            <div class="navbar-start">

                <!-- Logo -->
                <a href="/home" class="btn btn-ghost normal-case text-2xl text-neutral-focus ml-0 items-center">
                    <img class="w-12" src="/logo-textless.svg" alt="logo"/>
                    <p class="pt-1">Acordb</p>
                </a>

                <!-- Controls -->
                <div class="ml-4">
                    <a href="/search" class="btn btn-ghost">Procura Avançada</a>
                    <a href="/home#stats" class="btn btn-ghost">Estatísticas</a>
                </div>

            </div>


            <!-- Right Items -->
            <div class="navbar-end">

                {#if isAuthenticated}

                    <NavbarAuthSection {isAdmin}/>

                {:else}

                    <NavbarNoAuthSection/>

                {/if}

            </div>
        </div>
    </header>
</div>


<style>

    .navbar-shadow {
        @apply shadow-lg;
        @apply transition-shadow;
    }

    .navbar-shadow-out {
        @apply transition-shadow;
    }

</style>