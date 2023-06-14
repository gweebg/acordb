<script>
	import Metadados from "./Metadados.svelte";
    import Header from "./Metadados.svelte";
    export let data;
    let process = data.process;
    let record = data.record; 
    let fields = [];
    for (let key in record.data) {
        if (record.data.hasOwnProperty(key) && !(["id", "added_by", "added_at"].includes(key))) {
            if (typeof(record.data[key]) === 'string'){
                fields.push([key, record.data[key]]);
            }
            else {
                fields.push([key, record.data[key].join("\n")])
            }
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
    )
    function handleRowClick(id) {
        // Redirect to the link with the object ID
        window.location.href = `/record/${id}`;
    }
</script>

<div class="container mx-auto py-5">
    <div class="divider pt-3 pb-6">Dados</div>
    <div>
        <table class="table rounded-2xl shadow-lg w-full">
            <!-- head -->
            <thead>
                <tr>
                    <th class="bg-accent">Campo</th>
                    <th class="bg-accent">Valor</th>
                </tr>
            </thead>
            <tbody class="bg-card-accent">
                <!-- row 1 -->
                {#each fields as e}
                <tr class="bg-card-accent">
                    <th class="bg-card-accent">{e[0]}</th>
                    <td class="bg-card-accent whitespace-pre-wrap break-all">{e[1]}</td>
                </tr>
                {/each}
            </tbody>
        </table>
    </div>
    <div class="divider py-6">Metadados</div>
    <Metadados record={record}/>
    <div class="divider py-6">Versoes</div>
    <div>
        <table class="table rounded-2xl shadow-lg w-full">
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