<script>

    import {compareRulings} from "$lib/scripts/jsonDiff.js";
    import {onMount} from "svelte";
    import {PUBLIC_API_URL} from "$env/static/public";

    export let details;
    export let isAdmin;

    let diffHTML = '';

    const loadDiff = async (rulingId) => {

        let originalData;

        try {

            const response = await fetch(`${PUBLIC_API_URL}/acordaos/${rulingId}`,
                {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' },
                });

            if (response.ok) {
                originalData = await response.json();
            }
            else {
                console.log(`[Error ${response.status}] loadDiff @ RequestItem`);
            }

        } catch (err) {console.log(`[Error] loadDiff @ RequestItem ${err}`);}

        return compareRulings(originalData.data, details.data);

    }

    onMount(async () => {
        diffHTML = await loadDiff(details.acordao)
    });

</script>


<main>

    <div class="divider mt-0"></div>
    <header class="flex flex-row mt-4">
        <h1 class="text-lg">A ver diferenças entre o original e o sugerido:</h1>
        <div class="ml-auto">
            <div class="badge badge-accent">
                Adicionado
            </div>

            <div class="ml-2 badge badge-warning">
                Removido
            </div>
        </div>
    </header>

    <!-- Diff Viewer    -->
    <div class="flex flex-row my-4">

        <div class="scroll-container w-full mx-2 p-2 bg-base-100 rounded-xl max-h-[800px] overflow-y-scroll p-4">
            <div>
                {@html diffHTML}
            </div>
        </div>
    </div>


    <div class="flex items-center">

        <a href={"/record/" + details.acordao} class="text-xs opacity-80 underline">Ver detalhes do acórdão</a>


        {#if isAdmin}

            <form action="?/deny" method="POST" class="ml-auto mr-2">
                <input type="text" class="hidden" value={details.id} name="id">
                <button class="btn btn-sm btn-error">Rejeitar</button>
            </form>

            <form action="?/accept" method="POST">
                <input type="text" class="hidden" value={details.id} name="id">
                <button class="btn btn-sm btn-accent">Aceitar</button>
            </form>

        {/if}

    </div>

</main>