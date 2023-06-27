<script>
    export let list;

    list.map(
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
        window.location.href = `/ruling/${id}`;
    }

    console.log(list);

</script>

<table class="table table-zebra shadow-xl rounded-xl overflow-hidden">
    <!-- head -->
    <thead>
        <tr>
            {#each ["Added_At", "Added_By", "Processo" ,"Tribunal", "Relator", "Votação", "Meio Processual"] as r}
                <th class="bg-accent text-accent-content">{r}</th>
            {/each}
        </tr>
    </thead>
    <tbody class="bg-card-accent">
        <!-- row 1 -->
        {#each list as r}
            <a href={`/record/${r.id}`} on:click|preventDefault={() => handleRowClick(r.acordao)}  class="table-row hover:bg-base-200 transition duration-100">
                {#each [r.added_at, r.added_by, r.data.Processo ,r.data.tribunal, r.data.Relator, r.data["Votação"], r.data["Meio Processual"]] as valor}
                    <td class="whitespace-pre-wrap break-all">{valor}</td>
                {/each}
            </a>
        {/each}
    </tbody>
</table>