<script>

    import RecordsTable from "$lib/components/RecordsTable.svelte";
	
    let list = getRecentList();
    import { PUBLIC_API_URL } from '$env/static/public';
    async function getRecentList() {
        const res = await fetch(`${PUBLIC_API_URL}/acordaos?limit=10&sort=desc`);
        const obj = await res.json();

        if (res.ok) {
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


        <button class="btn btn-base-100 btn-sm mt-4 float-right">View All</button>

        {#await list}
            <p>...waiting</p>
        {:then plist}
            <RecordsTable list={plist} />
        {:catch error}
            <p style="color: red">{error.message}</p>
        {/await}

    </div>

</section>
