<script>

    import Select from "svelte-select";
    import TagsInput from "$lib/components/new/TagsInput.svelte";

    import {newForm} from "$lib/stores/form.js";
    import {addInput, removeInput} from "$lib/scripts/formHandler.js";

    export let fields;


</script>

<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">Informações Gerais</h2>
        <p class="opacity-50">Por favor tenta inserir o máximo de informação possível!</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Mandatory Fields -->
    <div class="flex flex-row gap-4">

        <!-- Process Number Input Field -->
        <div class="form-control w-full max-w-xs">

            <label class="label" for="process">
                <span class="label-text">Número do Processo (Obrigatório)</span>
            </label>

            <input
                    id="process"
                    type="text"
                    placeholder="Número do processo"
                    class="input input-bordered w-full max-w-xs"
                    bind:value={$newForm.process}
            />

        </div>

        <!-- Tags Input Field -->
        <div class="form-control w-full max-w-xs">
            <TagsInput/>
        </div>

        <!-- URL Input Field -->
        <div class="form-control flex-grow">
            <label class="label" for="url">
                <span class="label-text">URL (Opcional)</span>
            </label>

            <input id="url"
                   type="text"
                   placeholder="Link para DSGI"
                   class="input input-bordered w-full"
                   bind:value={$newForm.url}
            />
        </div>

    </div>

    <!-- Optional Fields -->
    <div>

        <div class="divider"><span class="opacity-50">Campos Opcionais</span></div>

        {#each $newForm.fields as field (field.id)}

            <div class="flex items-center">

                <div class="flex flex-row gap-2 my-2 w-full">
                    <div class="join w-full">

                        <div class="join-item">
                            <Select
                                    items={fields}
                                    placeholder="Escolhe um campo"
                                    --width="300px"
                                    --border-radius="0.5rem 0 0 0.5rem"
                                    --height="48px"
                                     bind:value={field.value.field}
                            />

                        </div>

                        <div class="flex-grow mr-4">
                            <div>
                                <input
                                        class="input input-bordered join-item w-full"
                                        placeholder="Insere um valor"
                                        bind:value={field.value.value}
                                />
                            </div>
                        </div>

                    </div>
                </div>

                <button type="button" class="btn btn-circle btn-xs ml-auto" on:click={() => removeInput(field.id)}>
                    <img src="/icons/cross.svg" alt="delete">
                </button>
            </div>

        {/each}

        <button type="button" class="btn w-full mt-4" on:click={addInput}>Novo Campo</button>

    </div>
</main>