<script>

    import Metadata from "$lib/components/record/Metadata.svelte";
    import TagsComp from "./tagsComp.svelte";
    export let data;

    let process = data.process;
    let record = data.record; 
    let fields = [];


    for (let key in record.data) {
        if (record.data.hasOwnProperty(key) && !(["id", "added_by", "added_at"].includes(key))) {
            fields.push([key, record.data[key]]);
        }
    }

    process.map(
        (r) => {
            if (r.data["Votação"] === undefined) {
                r.data["Votação"] = "Não disponível"
            }
            if (r.data["Relator"] === undefined) {
                r.data["Relator"] = "Não disponível"
            }
        }
    );

    function handleRowClick(id) {
        // Redirect to the link with the object ID.
        window.location.href = `/record/${id}`;
    }

</script>

<div class="container mx-auto py-5">

    <!-- General Data + Record URL  -->
    <div class="flex flex-row justify-between items-center">
        <h2 class="text-3xl font-bold">General Data</h2>
        <a href={"http://www.dgsi.pt/" + data.record.data.url} target="_blank" class="btn btn-outline btn-sm text-neutral stroke-neutral hover:stroke-neutral-content">
            <div class="pt-1">View Ruling</div>
            <svg class="stroke-inherit" width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">-->
                <path d="M13.0464 17C11.5404 15.4882 11.6761 12.9009 13.3494 11.2211L18.197 6.35462C19.8703 4.67483 22.4476 4.53865 23.9536 6.05046C25.4596 7.56228 25.3239 10.1496 23.6506 11.8294L21.2268 14.2626" stroke-width="1.5" stroke-linecap="round"/>-->
                <path d="M16.9536 13C18.4596 14.5118 18.3239 17.0991 16.6506 18.7789L14.2268 21.2121L11.803 23.6454C10.1297 25.3252 7.55237 25.4613 6.0464 23.9495C4.54043 22.4377 4.67609 19.8504 6.34939 18.1706L8.77323 15.7373" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
        </a>
    </div>

    <div class="divider"></div>

    <!-- General Data Table -->
    <div>
        <table class="table table-zebra shadow-xl rounded-xl overflow-hidden">
            <!-- Table Header -->
            <div class="table-header-group">
                <tr>
                    <th class="font-bold text-base   bg-accent text-accent-content">Field</th>
                    <th class="text-center text-base bg-accent text-accent-content">Value</th>
                </tr>
            </div>

            <!-- Table Content -->
            <tbody class="bg-card-accent">
                {#each fields as e}
                    <tr class="overflow-hidden">
                        <th class="whitespace-pre-wrap break-all">{e[0]}</th>
                        <td class="whitespace-pre-wrap break-all">{e[1]}</td>
                    </tr>
                {/each}
            </tbody>

        </table>
    </div>

    <!-- Metadata Header    -->
    <h2 class="text-3xl font-bold mt-12">Tags</h2>
    <div class="divider"></div>

    <!-- Metadata -->
    <TagsComp tags={record.tags} />

    <!-- Metadata Header    -->
    <h2 class="text-3xl font-bold mt-12">Metadata</h2>
    <div class="divider"></div>

    <!-- Metadata -->
    <Metadata record={record}/>

    <!-- Ruling Versions Header    -->
    <h2 class="text-3xl font-bold mt-12">Ruling Versions</h2>
    <div class="divider"></div>

    <div>
        <table class="table table-zebra shadow-xl rounded-xl overflow-hidden">
            <!-- head -->
            <thead>
                <tr>
                    {#each ["Added_At", "Added_By", "Tribunal", "Relator", "Votação"] as r}
                        <th class="bg-accent text-accent-content">{r}</th>
                    {/each}
                </tr>
            </thead>
            <tbody class="bg-card-accent">
                <!-- row 1 -->
                {#each process as r}
                <a href={`/record/${r.id}`} on:click|preventDefault={() => handleRowClick(r.id)}  class="table-row hover:bg-base-200 transition duration-100"> 
                    {#each [r.added_at, r.added_by, r.data.tribunal, r.data.Relator, r.data["Votação"]] as valor}
                        <td class="whitespace-pre-wrap break-all">{valor}</td>
                    {/each}
                </a>
                {/each}
            </tbody>
        </table>
    </div>
</div>