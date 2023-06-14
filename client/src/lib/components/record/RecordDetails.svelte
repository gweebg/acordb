<script>

    import Metadata from "$lib/components/record/Metadata.svelte";

    export let data;

    let process = data.process;
    let record = data.record; 
    let fields = [];


    for (let key in record.data) {
        if (record.data.hasOwnProperty(key) && !(["id", "added_by", "added_at"].includes(key))) {

            if (typeof(record.data[key]) === 'string') fields.push([key, record.data[key]]);
            else fields.push([key, record.data[key].join("\n")])

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
        <a href={"http://www.dgsi.pt/" + data.record.data.url} target="_blank" class="text-neutral underline">View Ruling</a>
    </div>
    <div class="divider"></div>

    <!-- General Data Table -->
    <div class="overflow-x-auto">
        <table class="table table-zebra w-full">

            <!-- Table Header -->
            <thead>
                <tr>
                    <th class="font-bold text-base bg-accent">Field</th>
                    <th class="text-center text-base bg-accent">Value</th>
                </tr>
            </thead>

            <!-- Table Content -->
            <tbody class="bg-card-accent">
                {#each fields as e}
                    <tr class="bg-card-accent">
                        <th class="bg-card-accent">{e[0]}</th>
                        <td class="bg-card-accent whitespace-pre-wrap break-all">{e[1]}</td>
                    </tr>
                {/each}
            </tbody>

        </table>
    </div>


    <!-- Metadata Header    -->
    <h2 class="text-3xl font-bold mt-12">Metadata</h2>
    <div class="divider"></div>

    <!-- Metadata -->
    <Metadata record={record}/>

    <!-- Ruling Versions Header    -->
    <h2 class="text-3xl font-bold mt-12">Ruling Versions</h2>
    <div class="divider"></div>

    <div>
        <table class="table table-zebra shadow-lg w-full">
            <!-- head -->
            <thead>
                <tr>
                    <th class="bg-accent">Added_At</th>
                    <th class="bg-accent">Added_By</th>
                    <th class="bg-accent">Tribunal</th>
                    <th class="bg-accent">Relator</th>
                    <th class="bg-accent">Votacao</th>
                </tr>
            </thead>
            <tbody class="bg-card-accent">
                <!-- row 1 -->
                {#each process as r}
                <a href={`/record/${r.id}`} on:click|preventDefault={() => handleRowClick(r.id)}  class="table-row hover:bg-base-100 transition duration-75"> 
                    <td class="bg-transparent whitespace-pre-wrap break-all">{r.added_at}</td>
                    <td class="bg-transparent whitespace-pre-wrap break-all">{r.added_by}</td>
                    <td class="bg-transparent whitespace-pre-wrap break-all">{r.data.tribunal}</td>
                    <td class="bg-transparent whitespace-pre-wrap break-all">{r.data.Relator}</td>
                    <td class="bg-transparent whitespace-pre-wrap break-all">{r.data["Votação"]}</td>
                </a>
                {/each}
            </tbody>
        </table>
    </div>
</div>