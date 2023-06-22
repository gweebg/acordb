<script>

    import {inputs, url, process} from "$lib/stores/form.js";

    import {addInput, removeInput, updateInput, updateSelectable} from "$lib/scripts/formHandler.js";

    import TagsInput from "$lib/components/new/TagsInput.svelte";
    import Select from "svelte-select";

    export let fields;


</script>

<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">General Information</h2>
        <p class="opacity-50">Please try to fill in as much data as possible.</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Mandatory Fields -->
    <div class="flex flex-row gap-4">

        <!-- Process Number Input Field -->
        <div class="form-control w-full max-w-xs">
            <label class="label" for="process">
                <span class="label-text">Process Number (Mandatory)</span>
            </label>

            <input
                    id="process"
                    type="text"
                    placeholder="Process Identification"
                    class="input input-bordered w-full max-w-xs"
                    bind:value={$process}
                    on:input={() => {process.set($process)}}
            />
        </div>

        <!-- Tags Input Field -->
        <div class="form-control w-full max-w-xs">
            <label class="label">
                <span class="label-text">Process Descriptors (Mandatory)</span>
            </label>

            <TagsInput/>
        </div>

        <!-- URL Input Field -->
        <div class="form-control flex-grow">
            <label class="label">
                <span class="label-text">URL (Optional)</span>
            </label>

            <input id="url"
                   type="text"
                   placeholder="DSGI link"
                   class="input input-bordered w-full"
                   bind:value={$url}
                   on:input={() => {url.set($url)}}/>
        </div>

    </div>

    <!-- Optional Fields -->
    <div>

        <div class="divider"><span class="opacity-50">Optional Fields</span></div>

        {#each $inputs as input (input.id)}

            <div class="flex items-center">


                <div class="flex flex-row gap-2 my-2 w-full">
                    <div class="join w-full">

                        <div class="join-item">
                            <Select
                                    items={fields}
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

                <button type="button" class="btn btn-circle btn-xs ml-auto" on:click={() => removeInput(input.id)}>
                    <img src="/icons/cross.svg" alt="delete">
                </button>
            </div>

        {/each}

        <button type="button" class="btn w-full mt-4" on:click={addInput}>Add Field</button>

    </div>
</main>