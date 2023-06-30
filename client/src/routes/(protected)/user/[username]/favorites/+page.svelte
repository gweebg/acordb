<script>

    import { page } from "$app/stores";

    import { initFlash } from "sveltekit-flash-message/client";
    import { toast, Toaster } from "svelte-french-toast";

    import FavoriteDetailBody from "$lib/components/dashboard/FavoriteDetailBody.svelte";
    import SideBar from "$lib/components/dashboard/SideBar.svelte";

    export let data;

    let visible = false;
    const flash = initFlash(page);

    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    let itemsChecked = Array(data.data.length).fill(false);
    let totalChecked = 0;

    $: {
        const noChecked = itemsChecked.every(e => e === false);
        visible = !noChecked;
    }

    $: totalChecked = itemsChecked.filter(e => e === true).length;

    $: if ($flash) {
    	switch ($flash.type) {
    		case "success":
    			toast.success($flash.message, toastStyle);
    			break;
    		case "error":
    			toast.error($flash.message, toastStyle);
    			break;
    	}
    }

    const openMultiple = () => {
        for (let i = 0; i < itemsChecked.length; i++) {
            if (itemsChecked[i] === true) window.open(`/ruling/${data.data[i].acordao}`, "_blank");
        }
    };

    const uncheckAll = () => {
        itemsChecked = itemsChecked.fill(false);
    }
    

</script>


<svelte:head>
    <title>Acordb - Favorites</title>
</svelte:head>


<Toaster/>

<div class="flex flex-row">

    <div class="fixed">
        <SideBar
                active={{profile: false, rulings: false, favourites: true, settings: false, requests: false}}
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

                <h2 class="text-xl flex justify-center">You should try adding some favorites!</h2>

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
                                    <h2 class="card-title">Favorite #{fav.id}</h2>
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

                                    <a href={"/ruling/" + fav.acordao} target="_blank" class="btn btn-accent btn-sm mt-2">
                                        <img src="/icons/hyperlink.svg" alt="redirect">
                                    </a>

                                    <input type="checkbox" id={fav.id} class="modal-toggle">

                                    <div class="modal">
                                        <FavoriteDetailBody favData={fav}/>
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

