<script lang="ts">
    export let query: any = {};
    import { onMount } from "svelte";
	import RecordsTable from "../RecordsTable.svelte";
    import { PUBLIC_API_URL } from '$env/static/public';
    let list: any[] = [];
    let loading = true;
    let items_per_page = 12;
    let currentPage = 1;
    let totalPages = 10;
    let visiblePages = [];

    const getSearchResults = async (query_params: object, page_number: number) => {
        page_number = page_number || 0;
        query_params["limit"] = items_per_page;
        query_params["skip"] = (page_number-1)*query_params["limit"];
        console.log(query_params);
        const response = await fetch(`${PUBLIC_API_URL}/acordaos?${new URLSearchParams(query_params)}`)
        const obj = await response.json();

        if (response.ok) {
            for (let i = 0; i < obj.length; i++) {
                let arr = ["Processo" ,"tribunal", "Relator", "Votação", "Meio Processual"];
                arr.forEach(
                    (v) => { if (obj[i].data[v] === undefined) obj[i].data[v] = "N/A" }
                )
            }
            return obj;
        } else throw new Error(obj);
    }

    const updateVisiblePages = () => {
        const maxVisiblePages = 5;
        const halfVisiblePages = Math.floor(maxVisiblePages / 2);
        let startPage = currentPage - halfVisiblePages;
        let endPage = currentPage + halfVisiblePages;

        if (startPage < 1) {
            startPage = 1;
            endPage = startPage + maxVisiblePages - 1;
        }

        if (endPage > totalPages) {
            endPage = totalPages;
            startPage = endPage - maxVisiblePages + 1;
            if (startPage < 1) {
                startPage = 1;
            }
        }

        visiblePages = Array(endPage - startPage + 1).fill().map((_, i) => startPage + i);
    };

    onMount(async () => {
        list = await getSearchResults(query, currentPage);
        updateVisiblePages();
        loading = false;
    })

    const goToPage = async (page: number) => {
        currentPage = page;
        loading = true;
        list = await getSearchResults(query, currentPage);
        updateVisiblePages();
        loading = false;
    };
</script>


{#if loading}
    <div class="flex justify-center items-center">
        <span class="loading loading-spinner text-primary loading-lg"></span>
    </div>
{:else}
    <RecordsTable list={list}/>

    <div class="join">
        {#each visiblePages as page}
            <button class="join-item btn pagination-item {currentPage === page ? 'btn-active' : ''}" on:click={() => goToPage(page)}>
                {page}
            </button>
        {/each}
    </div>
{/if}