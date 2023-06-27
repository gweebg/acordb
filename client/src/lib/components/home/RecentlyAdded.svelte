<script>

    import RecordsTable from "$lib/components/RecordsTable.svelte";
	
    import { PUBLIC_API_URL } from '$env/static/public';

    let list = getRecentList();
    async function getRecentList() {
        const res = await fetch(`${PUBLIC_API_URL}/acordaos?limit=10&sort=desc`);
        const obj = await res.json();

        if (res.ok) {
            
            for (let i = 0; i < obj.length; i++) {
                console.log(obj[i])
                let arr = ["Processo" ,"tribunal", "Relator", "Votação", "Meio Processual"]
                arr.forEach(
                    (v) => {
                        if (obj[i].data[v] === undefined) {
                            obj[i].data[v] = "N/A"
                        }
                    }
                )
            }
            return obj;
        } else {
            throw new Error(obj);
        }
    }

    function refreshList() {
        list = getRecentList();
    }

</script>

<section id="recently-uploaded" class="bg-neutral">

    <div class="px-4 py-20 my-[100px] mx-48">

        <h2 class="text-3xl font-bold text-white">Recently Uploaded Rulings</h2>

        <div class="opacity-60 text-white">
            <p>If the table did not update, please refresh the page!</p>
        </div>
        
        <div class="divider border-t border-white"></div>


        {#await list}

            <div class="flex justify-center items-center">
                <span class="loading loading-spinner text-primary loading-lg"></span>
            </div>

        {:then plist}

            <RecordsTable list={plist}/>

        {:catch error}

            <div class="flex justify-center items-center">
                <span class="loading loading-spinner text-primary"></span>
                <p class="text-error">{error.message}</p>
            </div>

        {/await}

        <button class="btn btn-base-100 btn-sm mt-4 float-right">View All</button>

    </div>

</section>
