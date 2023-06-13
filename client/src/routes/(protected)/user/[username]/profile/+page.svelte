<script>

    import SideBar from "$lib/components/dashboard/SideBar.svelte";

    export let data; // Data returned from the load function at +page.server.js

    const switchPassword = () => {

        const passwordInput = document.getElementById("password");

        if (passwordInput.type === "password") passwordInput.type = "text";
        else passwordInput.type = "password";

        const passwordIcon = document.getElementById("passwordIcon");

        if (passwordIcon.src.endsWith("eye-open.svg")) passwordIcon.src = "/icons/profile/eye-closed.svg";
        else passwordIcon.src = "/icons/profile/eye-open.svg";

    };

</script>



<div class="flex flex-row">

    <div class="fixed">
        <SideBar
            active={{profile: true, rulings: false, favourites: false, settings: false, add: false}}
            name={data.user.email}
            basePath={"/user/" + data.user.id}
            userRole={data.user.is_administrator}
        />
    </div>

    <!-- Content -->
    <div class="flex-1 h-screen p-12 overflow-y-auto ml-96">

        <!-- Header -->
        <header>

            <div class="text-sm breadcrumbs">
                <ul>
                    <li><p>Dashboard</p></li>
                    <li><p>Profile</p></li>
                </ul>
            </div>


            <h2 class="text-3xl font-bold">{data.user.first_name}'s Profile</h2>
            <div class="divider"></div>

        </header>

        <!-- Content -->
        <div class="flex flex-row">

            <!-- Account -->
            <div class="w-1/2 mr-12">

                <h3 class="text-xl font-bold pb-4">Your Account</h3>


                <form action="" method="POST">

                    <label class="label">
                        <span class="label-text">Email Address</span>
                    </label>
                    <input id="email"
                           disabled
                           type="text"
                           value={data.user.email}
                           class="input input-bordered w-full" />

                    <label class="label">
                        <span class="label-text">Username</span>
                    </label>
                    <input id="username"
                           type="text"
                           value={data.user.first_name + " " + data.user.last_name}
                           class="input input-bordered w-full" />

                    <label class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <div class="form-control">
                        <div class="input-group">
                            <input id="password"
                                   type="password"
                                   placeholder="Type a new password"
                                   class="input input-bordered w-full" />

                            <button type="button" class="btn btn-square btn-accent" on:click={switchPassword}>
                                <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                            </button>

                        </div>
                    </div>

                    <fieldset class="mt-6 float-right">
                        <button type="button" class="btn">Reset </button>
                        <button type="submit" class="btn btn-accent">Save Changes</button>
                    </fieldset>

                </form>

            </div>

            <!-- Stats -->
            <div class="w-1/2">

                <h3 class="text-xl font-bold pb-4">Your Stats</h3>

                <div class="flex gap-4">

                    <div class="stats shadow">

                        <div class="stat">
                            <div class="stat-title">Created at</div>
                            <div class="stat-value">{data.user.createdAt}</div>
                            <div class="stat-desc">Account creation date</div>
                        </div>

                    </div>

                    <div class="stats shadow">

                        <div class="stat">
                            <div class="stat-title">You added</div>
                            <div class="stat-value">{data.user.addedRecords}</div>
                            <div class="stat-desc">Rulings</div>
                        </div>

                    </div>

                    <div class="stats shadow">

                        <div class="stat">
                            <div class="stat-title">Favorites</div>
                            <div class="stat-value">{data.user.favorites}</div>
                        </div>

                    </div>



                </div>



            </div>

        </div>



        <!-- Save Controls -->
        <div class="">

        </div>

    </div>
</div>