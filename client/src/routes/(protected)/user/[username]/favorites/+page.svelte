<script>

    import SideBar from "$lib/components/dashboard/SideBar.svelte";
    import FavoriteDetailBody from "$lib/components/dashboard/FavoriteDetailBody.svelte";

    export let data; // Data returned from the load function at +page.server.js

    let visible = false;

    let itemsChecked = Array(data.data.length).fill(false);
    let totalChecked = 0;

    $: {
        const noChecked = itemsChecked.every(e => e === false);
        visible = !noChecked;
    }

    $: totalChecked = itemsChecked.filter(e => e === true).length;

    const openMultiple = () => {

        for (let i = 0; i < itemsChecked.length; i++) {
            if (itemsChecked[i] === true) window.open(`/process/${data.data[i].processo}`, "_blank");
        }

    };

    const uncheckAll = () => {
        itemsChecked = itemsChecked.fill(false);
    }

</script>


<div class="flex flex-row">

    <div class="fixed">
        <SideBar
                active={{profile: false, rulings: false, favourites: true, settings: false, add: false}}
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
                    <li><p>Favorites</p></li>
                </ul>
            </div>


            <h2 class="text-3xl font-bold">Bookmarked Rulings</h2>
            <div class="divider"></div>

        </header>

        <!-- Content -->
        <div class>

            <!-- Controls for when any favorite is selected via checkbox. -->
            {#if visible }
                <div class="flex w-full h-14 rounded-xl gap-2">

                    <p>{totalChecked} rulings selected</p>

                    <div class="ml-auto">
                        <button class="btn btn-sm btn-accent" on:click={openMultiple}>Open All</button>
                        <button class="btn btn-sm" on:click={uncheckAll}>Uncheck All</button>
                    </div>

                </div>
            {/if}

            <!-- If there is no favorites show alternative message. -->
            {#if data.data.length === 0}

                <h2 class="text-xl flex justify-center">You should try adding some favorites...</h2>

            {:else}

                <!-- Else put the favorites card. -->
                <div class="flex flex-wrap gap-6">

                    {#each data.data as fav, i}

                        <div class="card w-96 bg-base-100 shadow-lg overflow-ellipsis">
                            <div class="card-body">

                                <!-- Card Header -->
                                <div class="flex flex-row gap-2 items-center">
                                    <label>
                                        <input type="checkbox" class="checkbox mt-1" bind:checked={itemsChecked[i]}/>
                                    </label>
                                    <h2 class="card-title">Process {fav.processo}</h2>
                                </div>

                                <!-- Card Description -->
                                {#if fav.description.length === 0}
                                    <p class="opacity-40">No description available.</p>
                                {:else}
                                    <p class="overflow-hidden nowrap truncate">{fav.description}</p>
                                {/if}

                                <!-- Card Controls -->
                                <div class="card-actions justify-end">
                                    <label for={fav.id} class="btn btn-sm mt-2">Details</label>

                                    <a href={"/process/" + fav.processo} target="_blank" class="btn btn-accent btn-sm mt-2">
                                        <img src="/icons/hyperlink.svg" alt="redirect">
                                    </a>

                                    <input type="checkbox" id={fav.id} class="modal-toggle">

                                    <div class="modal">
                                        <FavoriteDetailBody favData={fav} auth={data.token}/>
                                    </div>
                                </div>

                            </div>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>
    </div>
</div>

