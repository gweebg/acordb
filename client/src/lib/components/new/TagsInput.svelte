<script>

    import {tags} from "$lib/stores/form.js";

    let inputValue = '';

    const addTag = () => {

        let newTags;

        const unsub = tags.subscribe((tagList) => {

            const val = inputValue.trim();
            if (val !== '' && !tagList.includes(val)) {
                newTags = [...tagList, val];
                inputValue = '';
            }

        });

        unsub();

        tags.set(newTags);

    }

    const removeTag = (tag) => {

        let filteredTags;

        const unsub = tags.subscribe((tagList) => {
            filteredTags = tagList.filter(t => t !== tag);
        });

        unsub();

        tags.set(filteredTags);

    }

    const handleInputKeydown = (event) => {

        /* If Enter is pressed we add a new tag. */
        if (event.key === 'Enter' || event.key === ',') {
            event.preventDefault();
            addTag();
        }
    }


</script>

<div class="flex flex-col mb-2">

    <input
            type="text"
            bind:value={inputValue}
            placeholder="Enter a descriptor"
            class="input input-bordered w-full max-w-xs"
            on:keydown={handleInputKeydown}
    />

    <div class="flex flex-wrap mb-2">
        {#each $tags as tag}
            <div class="mt-2 bg-base-100 rounded flex items-center px-2 py-1 mr-1 mb-1">
                <span>{tag}</span>
                <button class="cursor-pointer ml-2" on:click={() => removeTag(tag)}>×</button>
            </div>
        {/each}
    </div>

</div>
