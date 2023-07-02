<script>

    import { createEventDispatcher } from "svelte";

    export let tags = [];
    let inputValue = "";

    const dispatch = createEventDispatcher();

    const handleInput = (event) => {
        inputValue = event.target.value;
    }

    const handleKeyDown = (event) => {
        if (event.key === "Enter" && inputValue.trim() !== "") {

            const newTag = inputValue.trim();
            if (!tags.includes(newTag)) {
                tags = [...tags, newTag];
            }
            inputValue = "";
            event.preventDefault();

        } else if (event.key === "Backspace" && inputValue === "" && tags.length > 0) {
            tags = tags.slice(0, -1);
        }
    }

    const removeTag = (index) => {
        tags = tags.filter((_, i) => i !== index);
    }

    $: {
        dispatch("tagsChange", tags);
    }

</script>

<div class="flex flex-wrap items-center input input-bordered">
    {#each tags as tag, index}
        <div class="badge badge-info text-white tag" on:click={() => removeTag(index)}>
            {tag}
            <span class="tag-remove">x</span>
        </div>
    {/each}
    <input
            class="input input-ghost focus:outline-none m-0 p-0 flex-grow"
            type="text"
            placeholder="Adiciona descritores"
            value={inputValue}
            on:input={handleInput}
            on:keydown={handleKeyDown}
    />
</div>

<style>

    .tag {
        display: flex;
        align-items: center;
        margin-right: 4px;
        margin-bottom: 4px;
        font-size: 14px;
        cursor: pointer;
    }

    .tag-remove {
        margin-left: 4px;
        cursor: pointer;
    }

</style>
