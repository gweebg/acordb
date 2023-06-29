<script>
    export let list = [];
    function handleRowClick(id) {
        // Redirect to the link with the object ID.
        window.location.href = `/ruling/${id}`;
    }
    for (let i = 0; i < list.length; i++) {
        let arr = ["Processo" ,"tribunal", "Relator", "Votação", "Meio Processual"];
        arr.forEach(
            (v) => { if (list[i].data[v] === undefined) list[i].data[v] = "N/A" }
            )
    }
</script>

<table class="table table-zebra shadow-xl rounded-xl overflow-hidden">

    <!-- Table Header -->
    <thead>
        <tr>
            {#each ["Added At", "Added By", "Processo" ,"Tribunal", "Relator", "Votação", "Meio Processual"] as r}
                <th class="bg-accent text-accent-content">{r}</th>
            {/each}
        </tr>
    </thead>

    <!-- Table Rows -->
    <tbody class="bg-card-accent">
        {#each list as r}
            <td on:click|preventDefault={() => handleRowClick(r.acordao)}  class="table-row hover:bg-base-200 transition duration-100 cursor-pointer">
                {#each [r.added_at, r.added_by, r.data.Processo ,r.data.tribunal, r.data.Relator, r.data["Votação"], r.data["Meio Processual"]] as valor}
                    <td class="whitespace-pre-wrap break-all">{valor}</td>
                {/each}
            </td>
        {/each}
    </tbody>

</table>