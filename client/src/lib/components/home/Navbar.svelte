<script>

    // export let isAuth;
    let windowY;

</script>

<svelte:window bind:scrollY={windowY}/>

<div class="bg-base-100 sticky top-0 z-50 {windowY > 1 ? 'navbar-shadow' : 'navbar-shadow-out'}">

    <header id="navbar" class="header-area mx-48">

        <!-- Navbar -->
        <div class="navbar border-none px-4">

            <!-- Left Items -->
            <div class="navbar-start">

                <!-- Logo -->
                <a href="/home" class="btn btn-ghost normal-case text-2xl text-neutral-focus ml-0">
                    Accordb
                </a>

                <!-- Controls -->
                <div class="ml-4">
                    <a href="/home" class="btn btn-ghost">Advanced Search</a>
                    <a href="#stats" class="btn btn-ghost">Statistics</a>
                </div>

            </div>


            <!-- Center Items -->
            <div class="navbar-center">
                <!-- Simple Search Bar -->
                <input type="text" placeholder="Begin search..." class="input input-bordered input-sm w-full max-w-xs" />
            </div>

            <!-- Right Items -->
            <div class="navbar-end">
                <div class="flex gap-4 items-center">

                    <!-- Add New Button -->
                    <button class="btn btn-sm btn-accent">NEW</button>

                    <!-- Dashboard Button -->
                    <button class="btn btn-outline btn-sm">Dashboard</button>

                    <div class="dropdown dropdown-end">

                        <!-- Avatar / Hamburger Menu -->
                        <label tabindex="0" class="btn btn-ghost btn-circle avatar">
                            <div class="w-10 rounded-full">
                                <img src="/logo-textless.svg" />
                            </div>
                        </label>

                        <!-- Menu Items -->
                        <ul tabindex="0" class="mt-3 p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                            <li><a href="/">Profile</a></li>
                            <li><a href="/">Settings</a></li>
                            <li><a href="/">Logout</a></li>
                        </ul>

                    </div>
                </div>
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