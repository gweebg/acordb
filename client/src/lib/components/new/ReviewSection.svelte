<script>

    import {body, inputs, url, tags, process} from "$lib/stores/form.js";

    const tagsAsString = () => {

        let result = "";

        const unsubscribe = tags.subscribe((tagList) => {
            result = tagList.toString();
        });

        unsubscribe();
        return result;
    }

</script>


<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">Review & Submit</h2>
        <p class="opacity-50">Make sure to review every field of the ruling before submitting!</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Review Text -->
    <div class="mb-2 text-md">

        <section>

            <p><span class="font-bold text-neutral mb-2">Processo:</span> {$process}</p>

            <p><span class="font-bold text-neutral mb-2">Descritores:</span> {tagsAsString()}</p>

            {#if $inputs.length > 0}
                {#each $inputs as input}

                    <p><span class="font-bold text-neutral mb-2">{input.value.selectable.value}:</span> {input.value.input}</p>

                {/each}
            {/if}

        </section>

        <section>

            <div class="divider"><span class="opacity-50">Decision</span></div>
            {#if $body.decision !== ''}
                <p>{$body.decision}</p>
            {:else}
                <p>N/A</p>
            {/if}



            <div class="divider"><span class="opacity-50">Summary</span></div>
            {#if $body.summary !== ''}
                <p>{$body.summary}</p>
            {:else}
                <p>N/A</p>
            {/if}


            <div class="divider"><span class="opacity-50">Integral Text</span></div>
            {#if $body.text !== ''}
                <p>{$body.text}</p>
            {:else}
                <p>N/A</p>
            {/if}

        </section>

    </div>

</main>