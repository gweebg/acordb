<script>

    import {newForm} from "$lib/stores/form.js";

</script>


<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">Conteúdo do Acórdão</h2>
        <p class="opacity-50">Aqui, podes especificar o sumário, decisão e texto integral do acódão.</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Inputs -->
    <div class="mb-2">

        <!-- Decision -->
        <div class="form-control">
            <label class="label" for="decision">
                <span class="label-text">Decisão do Acordão</span>
            </label>
            <textarea
                    bind:value={$newForm.body.decision}
                    id="decision"
                    class="textarea textarea-bordered h-24"
                    placeholder="Aqui podes especificar a decisão do acórdão"></textarea>
        </div>


        <!-- Summary -->
        <div class="form-control">
            <label class="label" for="summary">
                <span class="label-text">Sumário</span>
            </label>
            <textarea
                    bind:value={$newForm.body.summary}
                    id="summary"
                    class="textarea textarea-bordered h-24"
                    placeholder="Aqui podes especificar o sumário do acórdão"></textarea>
        </div>

        <!-- Summary -->
        <div class="form-control">
            <label class="label" for="text">
                <span class="label-text">Texto Integral</span>
            </label>
            <textarea
                    bind:value={$newForm.body.text}
                    id="text"
                    class="textarea textarea-bordered h-24"
                    placeholder="Aqui podes especificar o texto integral do acórdão"></textarea>
        </div>

    </div>


    <small class="text-warning pt-4">(!) Repara que todos os campos acima são opcionais.</small>
</main>