<script>

    import AdvancedSearchForm from "$lib/components/AdvancedSearchForm.svelte";
    import RecentlyAdded from "$lib/components/RecentlyAdded.svelte";

    import { fade } from 'svelte/transition';

    let windowY;

</script>

<svelte:window bind:scrollY={windowY}/>

<div class="">

    <div class="bg-base-100 sticky top-0 z-50 {windowY > 1 ? 'navbar-shadow' : 'navbar-shadow-out'}" transition:fade>

        <header id="navbar" class="header-area mx-48">

            <!-- Navbar -->
            <div class="navbar border-none px-4">

                <!-- Left Items -->
                <div class="navbar-start">

                    <a href="/home" class="btn btn-ghost normal-case text-2xl text-neutral-focus ml-0">
                        Accordb
                    </a>

                    <!-- Controls -->
                    <div class="ml-4">
                        <button class="btn btn-ghost">Advanced Search</button>
                        <button class="btn btn-ghost">Statistics</button>
                    </div>


                </div>


                <!-- Center Items -->
                <div class="navbar-center">

                    <input type="text" placeholder="Begin search..." class="input input-bordered input-sm w-full max-w-xs" />

                </div>

                <!-- Right Items -->
                <div class="navbar-end">

                    <div class="flex gap-4 items-center">

                        <button class="btn btn-sm btn-accent">
                            NEW
                        </button>

                        <button class="btn btn-outline btn-sm">Dashboard</button>

                        <div class="dropdown dropdown-end">
                            <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                                <div class="w-10 rounded-full">
                                    <img src="/logo-textless.svg" />
                                </div>
                            </label>
                            <ul tabindex="0" class="mt-3 p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                                <li>
                                    <a class="justify-between">
                                        Profile
                                        <span class="badge">New</span>
                                    </a>
                                </li>
                                <li><a>Settings</a></li>
                                <li><a>Logout</a></li>
                            </ul>
                        </div>
                    </div>

                </div>

            </div>

        </header>

    </div>


    <!-- Main content -->
    <div class="">

        <!-- Advanced Search -->
        <AdvancedSearchForm/>

        <!-- Recently Added Rulings -->
        <RecentlyAdded/>

    </div>
    
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