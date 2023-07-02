<script>

    import RecordsTable from "$lib/components/RecordsTable.svelte";
	
    import { PUBLIC_CLIENT_API_URL } from '$env/static/public';
    import { onMount } from "svelte";

    let list = [];
    let loading = true;

    const getRecentList = async () => {

        const response = await fetch(`${PUBLIC_CLIENT_API_URL}/acordaos/?limit=10&sort=desc`);
        let obj = await response.json();
        obj = obj.data;

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

    onMount(async () => {
        list = await getRecentList();
        loading = false;
    })

</script>

<section id="recently-uploaded" class="bg-neutral">

    <div class="px-4 py-20 my-[100px] mx-48">

        <div class="flex items-center justify-between">
            <div class="">
                <h2 class="text-3xl font-bold text-white">Acórdãos Adicionados Recentemente</h2>

                <div class="opacity-60 text-white">
                    <p>Se esta tabela não atualizou, experimenta re-carregar a página!</p>
                </div>
            </div>
            <a class="btn btn-outline btn-primary btn-sm mx-4" href="/search?sort=desc">Ver Todos</a>
        </div>


        <div class="divider border-t border-white"></div>

        {#if loading}
            <div class="flex justify-center items-center">
                <span class="loading loading-spinner text-primary loading-lg"></span>
            </div>
        {:else}
            <RecordsTable {list}/>
        {/if}

    </div>

</section>
