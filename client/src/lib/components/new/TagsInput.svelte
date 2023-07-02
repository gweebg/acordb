<script>

    import {newForm} from "$lib/stores/form.js";
    import {normalizeString} from "$lib/scripts/utils.js";

    let inputValue = '';

    const addTag = () => {

        let newTags;

        const unsub = newForm.subscribe((formData) => {

            const val = normalizeString(inputValue).trim();
            if (val !== '' && !formData.tags.includes(val)) {
                newTags = [...formData.tags, val];
                inputValue = '';
            }

        });

        unsub();

        newForm.update(formData => {
            return {...formData, tags: newTags}
        })

    }

    const removeTag = (tag) => {

        newForm.update(formData => {

            return {
                ...formData,
                tags: formData.tags.filter(t => t !== tag)
            }

        });

    }

    const handleInputKeydown = (event) => {

        /* If Enter is pressed we add a new tag. */
        if (event.key === 'Enter') {
            event.preventDefault();
            addTag();
        }
    }


</script>

<main>
    <label class="label" for="tags">
        <span class="label-text">Descritores (Obrigatório)</span>
    </label>

    <div class="flex flex-col mb-2">

        <input
                name="tags"
                id="tags"
                type="text"
                bind:value={inputValue}
                placeholder="Insere múltiplos descritores"
                class="input input-bordered w-full max-w-xs"
                on:keydown={handleInputKeydown}
        />

        <div class="flex flex-wrap mb-2">
            {#each $newForm.tags as tag}
                <div class="mt-2 badge badge-info text-white  flex items-center px-2 py-1 mr-1 mb-1">
                    <span>{tag}</span>
                    <button class="cursor-pointer ml-2" on:click={() => removeTag(tag)}>×</button>
                </div>
            {/each}
        </div>

    </div>
</main>
