<script>
    import ContentSection from "$lib/components/new/ContentSection.svelte";
    import GeneralSection from "$lib/components/new/GeneralSection.svelte";
    import ReviewSection from "$lib/components/new/ReviewSection.svelte";
    import Footer from "$lib/components/Footer.svelte";
    import Navbar from "$lib/components/home/Navbar.svelte";

    import {newForm} from "$lib/stores/form.js";
    import jsonToFormData from "@ajoelp/json-to-formdata";
    import {goto} from "$app/navigation";

    export let data;

    let sections = { general: true, content: false, details: false };
    let error = "";
    let modalError = "";
    let files;

    let buttonState = {
        content: "Próximo",
        isDisabled: true
    }

    const nextSection = () => {

        if (sections.general === true && sections.content === true) {

            const button = document.getElementById('submit');

            sections.details = true;
            buttonState.content = "Submeter";

            button.addEventListener('click', function() {
                button.setAttribute('type', 'submit');
            });

        }
        else if (sections.general === true) {
            sections.content = true;
            buttonState.isDisabled = false;
        }

        error = "";
    }

    const prevSection = () => {

        if (sections.details && sections.content && sections.general) {
            sections.details = false;
        } else if (sections.general && sections.content && !sections.details) {
            sections.content = false;
            buttonState.isDisabled = true;
        }

        const button = document.getElementById('submit');
        button.addEventListener('click', function() {
            button.setAttribute('type', 'button');
        });

        buttonState.content = "Próximo";

        error = "";
    }

    const handleSubmit = async (event) => {

        event.preventDefault();

        let data = {};

        const unsubscribe = newForm.subscribe(formData => data = {...formData});
        unsubscribe();

        data.fields = data.fields.map(field => {
            return {

                id: field.id,
                value: {
                    field: field.value.field.value,
                    value: field.value.value
                }

            }
        });

        const formData = jsonToFormData(data);

        const response = await fetch('?/new', {
            method: 'POST',
            body: formData
        });

        let result = await response.json();
        if (result.type === "failure") {

            prevSection(); prevSection();
            error = result.data.slice(1, -1).slice(1, -1);

        }

        else {
            const id = result.data.slice(1, -1).slice(1, -1);
            await goto(`/ruling/${id}`);
        }
    }

    const handleUpload = async (event) => {

        event.preventDefault();

        let file;
        let data = {};

        if (files && files.length > 0) {

            file = files[0];

            const reader = new FileReader();
            reader.readAsText(file);

            await new Promise(resolve => reader.onload = () => resolve());
            data = JSON.parse(reader.result);

            const formData = jsonToFormData(data);

            const response = await fetch('?/upload', {
                method: 'POST',
                body: formData
            });

            let result = await response.json();

            if (result.type === "failure") modalError = result.data.slice(1, -1).slice(1, -1);
            else {
                const id = result.data.slice(1, -1).slice(1, -1);
                await goto(`/ruling/${id}`);
            }
        }
    }

</script>

<svelte:head>
    <title>
        Novo Acórdão
    </title>
</svelte:head>

<div>

    <Navbar isAuthenticated={true} isAdmin={data.user.is_administrator}/>

    <!-- New judgment form. -->
    <div class="px-4 mb-[100px] mt-[80px] mx-48">

        <!-- Header (Text & Steps) -->
        <header class="flex flex-row">

            <!-- Text -->
            <div>
                <h2 class="text-3xl font-bold">Adiciona Um Novo Acórdão!</h2>
                <p class="opacity-50">Presta atenção aos campos obrigatórios!</p>
            </div>

            <!-- Steps -->
            <div class="ml-auto">
                <ul class="steps">
                    <li class="step {sections.general ? 'step-primary' : ''}">Informações Gerais</li>
                    <li class="step {sections.content ? 'step-primary' : ''}">Conteúdo</li>
                    <li class="step {sections.details ? 'step-primary' : ''}">Rever e Submeter</li>
                </ul>
            </div>

        </header>

        <div class="divider"></div>

        <form class="flex justify-center flex-col" id="new" action="?/new" method="POST" on:submit={handleSubmit}>

            <!-- Form Content -->
            <div>
                {#if sections.details === true}

                    <ReviewSection/>

                {:else if sections.content === true}

                    <ContentSection/>

                {:else}

                    <GeneralSection fields={data.fields}/>
                    
                {/if}
            </div>

            {#if error.length > 0}
                <p class="text-error text-sm">{error}</p>
            {/if}

            <div class="flex flex-row mt-4">

                <button class="btn" type="button" onclick="my_modal_3.showModal()">Adicionar Ficheiro</button>
                <dialog id="my_modal_3" class="modal">
                    <div class="modal-box">

                        <form method="dialog">
                            <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
                        </form>

                        <h3 class="font-bold text-lg">Carregar um acórdão:</h3>
                        <p class="opacity-50 text-sm">O ficheiro tem de ser um ficheiro JSON.</p>
                        <div class="divider m-0"></div>

                        <form action="?/upload" method="POST" class="my-4" on:submit={handleUpload}>
                            <input type="file" accept=".json" bind:files class="file-input file-input-bordered file-input-primary w-full">
                            <div class="flex flex-row">
                                <button class="btn btn-sm ml-auto mt-4 mb-0 w-full">Carregar</button>
                            </div>
                        </form>

                        {#if modalError.length > 0}
                            <p class="text-error text-sm mt-2">{modalError}</p>
                        {/if}

                    </div>
                </dialog>

                <!-- Next/Submit Button -->
                <div class="ml-auto">
                    <button id="back" disabled={buttonState.isDisabled} type="button" class="btn" on:click={prevSection}>Voltar</button>
                    <button id="submit" class="btn btn-primary" type="button" on:click={nextSection}>{buttonState.content}</button>
                </div>
            </div>

        </form>

    </div>

    <Footer/>

</div>





