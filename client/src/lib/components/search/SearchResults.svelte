<script lang="ts">

    import { onMount } from "svelte";
	import RecordsTable from "../RecordsTable.svelte";
    import { PUBLIC_API_URL } from '$env/static/public';
    import Ruling from "$lib/components/ruling/Ruling.svelte";

    export let query: any = {};

    let list: any[] = [];
    let loading = true;
    let items_per_page = 10;
    let currentPage = 1;
    let totalPages = 0;
    let visiblePages = 10;
    let totalCount = 0;

    let pages = [];

    const getSearchResults = async (query_params: object, page_number: number) => {

        page_number = page_number || 0;

        query_params["limit"] = items_per_page;
        query_params["skip"] = (page_number-1)*query_params["limit"];

        const response = await fetch(`${PUBLIC_API_URL}/acordaos?${new URLSearchParams(query_params)}`)
        const obj = await response.json();

        if (response.ok) {
            return obj;
        } else throw new Error(obj);
    }

    const updateVisiblePages = async () => {
        loading = true;
        let res = await getSearchResults(query, currentPage);
        list = res["data"];
        totalCount = res["count"];
        totalPages =  Math.ceil(res["count"] / items_per_page)
        

        let pageArray = [];
        if (currentPage < 7) {
            let range = visiblePages - 3
            for (let i = 1; i <= range; i++) {
                pageArray.push(i);
            }
            pageArray.push('...');
            pageArray.push(totalPages-1);
            pageArray.push(totalPages);
        }
        else if (currentPage > totalPages - 6) {
            let range = visiblePages - 3
            pageArray.push(1);
            pageArray.push(2);
            pageArray.push('...');
            for (let i = totalPages - range; i <= totalPages; i++) {
                pageArray.push(i);
            }
        }
        else {
            let range = visiblePages - 6
            pageArray.push(1);
            pageArray.push(2);
            pageArray.push('...');
            for (let i = currentPage - range/2; i <= currentPage + range/2; i++) {
                pageArray.push(i);
            }
            pageArray.push('...');
            pageArray.push(totalPages-1);
            pageArray.push(totalPages);
        }

        pages = pageArray;
        loading = false;
    }

    onMount(async () => {
        await updateVisiblePages();
    })

    const goToPage = async (page: number) => {
        currentPage = page;
        await updateVisiblePages();
    };

</script>


<main>

    <div class="mx-48 mb-16">

        <header class="flex flex-row items-center">
            <h1 class="text-3xl font-bold">Search Results</h1>
            {#if !loading}
                <p class="ml-auto opacity-70">({totalCount} results spread over {totalPages} pages)</p>
            {/if}
        </header>
        <div class="divider mt-0"></div>

        {#if loading}

            <div class="flex justify-center items-center">
                <span class="loading loading-spinner text-primary loading-lg"></span>
            </div>

        {:else}

            {#each list as ruling}

                <div class="my-4">
                    <Ruling {ruling}/>
                </div>

            {/each}


            <!-- Pagination Controls -->
            <div class="flex w-full justify-center my-6">
                <div class="join">

                    {#if currentPage > 1}
                        <button class="join-item btn" on:click={() => goToPage(currentPage-1)}>
                            &lt;
                        </button>
                    {:else}
                        <button class="join-item btn btn-disabled">&lt;</button>
                    {/if}

                    {#each pages as page}
                        {#if page === '...'}
                            <button class="join-item btn btn-disabled">...</button>
                        {:else}
                            <button class="join-item btn  {currentPage === page ? 'btn-active' : ''}" on:click={() => goToPage(page)}>
                                {page}
                            </button>
                        {/if}
                    {/each}

                    {#if currentPage < totalPages}
                        <button class="join-item btn" on:click={() => goToPage(currentPage+1)}> &gt;</button>
                    {:else}
                        <button class="join-item btn btn-disabled"> &gt;</button>
                    {/if}

                </div>
            </div>

        {/if}
    </div>

</main>

