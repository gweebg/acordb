<script>


    import { createEventDispatcher } from 'svelte';
    import {normalizeString} from "$lib/scripts/utils.js";

    export let ruling;

    let threshold = 150;

    let dispatch = createEventDispatcher();
    let rulingParams = Object.keys(ruling);

    let inputs = {};
    let fields = {};
    for (const param in rulingParams) {
        inputs[param] = false;
        fields[param] = false;
    }

    function handleClick(param, field = false) {
        if (!field) inputs[param] = true;
        else fields[param] = true;
    }

    function handleBlur(param) {
        inputs[param] = false;
        fields[param] = false;
        dispatch('valueChange', ruling);
    }

    const handleInput = (param, field = false) => {

        if (!field) {

            if (param === "Descritores") {
                ruling[param] = ruling[param].split(",").map((tag) => normalizeString(tag));
            }
        }
    }

    const deleteField = (param) => {

        rulingParams = rulingParams.filter(field => field !== param);
        delete inputs[param];
        delete ruling[param];

        dispatch('valueChange', ruling);
    }

    let fieldName = "";
    let fieldValue = "";
    let error = "";

    const newField = () => {

        if (fieldName.trim() === "") {
            error = "Field name is required!";
            return;
        }

        if (fieldValue.trim() === "") fieldValue = "New field";

        rulingParams.push(fieldName);
        ruling[fieldName] = fieldValue;
        inputs[fieldName] = true;

        fieldName = "";
        fieldValue = "";
        error = "";

        dispatch('valueChange', ruling);
        document.getElementById("addF").close();
    }

</script>

<main class="mt-4">

    {#each rulingParams as param}

        <div class="mb-8 bg-base-200 rounded-lg p-4">

            <header class="flex flex-row gap-2 items-center">

                <div class="pt-1">
                    <button type="button" class="btn btn-xs btn-neutral btn-circle" on:click={() => deleteField(param)}>
                        <img src="/icons/delete.svg" alt="remove">
                    </button>
                </div>

                <div class="">

                    <h3 class="font-bold text-lg">{param}</h3>

                </div>

            </header>

            {#if !inputs[param]}

                {#if ruling[param].length > threshold}

                    <pre on:dblclick={() => handleClick(param)} class="break-words whitespace-pre-wrap mt-2 opacity-70">{ruling[param]}</pre>

                {:else}
                    <p on:dblclick={() => handleClick(param)} class="mt-2 opacity-70">{ruling[param]}</p>
                {/if}

            {:else}

                {#if ruling[param].length > threshold}

                    <textarea
                            name={param}
                            class="input input-bordered w-full mt-2 height-auto"
                            id={param}
                            type="text"
                            bind:value={ruling[param]}
                            on:blur={() => handleBlur(param)}
                            on:input={() => handleInput(param)}
                    ></textarea>

                {:else}

                    <input
                            name={param}
                            class="input input-bordered w-full mt-2"
                            id={param}
                            type="text"
                            bind:value={ruling[param]}
                            on:blur={() => handleBlur(param)}
                            on:input={() => handleInput(param)}
                    />

                {/if}

            {/if}

        </div>

    {/each}

    <button type="button" onclick="addF.showModal()" class="btn btn-sm"><span class="">New Field +</span></button>

    <dialog id="addF" class="modal modal-bottom sm:modal-middle">

        <div class="modal-box">

            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                <header>
                    <h3 class="font-bold text-lg">Create a new field</h3>
                    <p class="text-sm opacity-70">Provide at least a field name.</p>
                    <div class="divider m-0"></div>
                </header>

            </form>

            <div class="flex flex-grow gap-2">

                <div class="form-control w-full max-w-xs">
                    <label class="label">
                        <span class="label-text">Field Name</span>
                    </label>
                    <input type="text" placeholder="Field Name" class="input input-bordered w-full" bind:value={fieldName} />
                </div>

                <div class="form-control w-full max-w-xs">
                    <label class="label">
                        <span class="label-text">Field Value</span>
                    </label>
                    <input type="text" placeholder="Field Name" class="input input-bordered w-full" bind:value={fieldValue} />
                </div>

            </div>

            {#if error.length > 5}

                <small class="text-error">{error}</small>

            {/if}

            <div class="modal-action">
                <button type="button" class="btn btn-sm btn-accent" on:click={newField}>
                    Create
                </button>
            </div>

        </div>
    </dialog>


</main>