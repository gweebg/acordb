<script>
    import Select from 'svelte-select';
    import {updateSelectable, updateInput} from "$lib/scripts/formHandler.js";

    export let input;
    export let fields;

    let collection = [
        { value: 1, label: 'Contencioso' },
        { value: 2, label: 'Acordão' },
        { value: 3, label: 'Votação' },
    ];

</script>


<div class="flex flex-row gap-2 my-2 w-full">
    <div class="join w-full">

        <div class="join-item">
            <Select
                    items={collection}
                    placeholder="Select ruling field"
                    --width="300px"
                    --border-radius="0.5rem 0 0 0.5rem"
                    --height="48px"
                    bind:value={input.value.selectable}
                    on:change={() => updateSelectable(input.id, input.value.selectable)}
            />
        </div>

        <div class="flex-grow mr-4">
            <div>
                <input
                        class="input input-bordered join-item w-full"
                        placeholder="Field value"
                        bind:value={input.value.input}
                        on:input={() => updateInput(input.id, input.value.input)}
                />
            </div>
        </div>

    </div>
</div>


