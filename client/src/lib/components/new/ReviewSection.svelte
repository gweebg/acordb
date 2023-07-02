<script>

    import {newForm} from "$lib/stores/form.js";

    const tagsAsString = () => {

        let result = "";

        const unsubscribe = newForm.subscribe((formData) => {
            result = formData.tags.toString();
        });

        unsubscribe();
        return result;
    }

</script>


<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">Rever e Submenter</h2>
        <p class="opacity-50">Não te esqueças de rever todos os campos antes de submeter!</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Review Text -->
    <div class="mb-2 text-md">

        <section>

            <p><span class="font-bold text-neutral mb-2">Processo:</span> {$newForm.process}</p>

            <p><span class="font-bold text-neutral mb-2">Descritores:</span> {tagsAsString()}</p>

            {#if $newForm.fields.length > 0}
                {#each $newForm.fields as input}

                    <p><span class="font-bold text-neutral mb-2">{input.value.field.value}:</span> {input.value.value}</p>

                {/each}
            {/if}

        </section>

        <section>

            <div class="divider"><span class="opacity-50">Decisão</span></div>
            {#if $newForm.body.decision !== ''}
                <p>{$newForm.body.decision}</p>
            {:else}
                <p>N/A</p>
            {/if}



            <div class="divider"><span class="opacity-50">Sumário</span></div>
            {#if $newForm.body.summary !== ''}
                <p>{$newForm.body.summary}</p>
            {:else}
                <p>N/A</p>
            {/if}


            <div class="divider"><span class="opacity-50">Texto Integral</span></div>
            {#if $newForm.body.text !== ''}
                <p>{$newForm.body.text}</p>
            {:else}
                <p>N/A</p>
            {/if}

        </section>

    </div>

</main>