<script>

    import { toast } from "svelte-french-toast";
    import SuggestionPreview from "$lib/components/sugestion/SuggestionPreview.svelte";
    import jsonToFormData from "@ajoelp/json-to-formdata";

    export let ruling;
    export let id;

    let changedRuling = ruling;

    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    const submitSuggestion = async (event) => {

        event.preventDefault();

        changedRuling.id = id;
        const formData = jsonToFormData(changedRuling);

        await fetch('?/suggest', {
            method: 'POST',
            body: formData
        });

        toast.success("Pedido enviado com sucesso!", toastStyle);
        document.getElementById("sug").close();

    }

    const handleChange = (event) => {
        changedRuling = event.detail
    }


</script>

<main>

    <div onclick="sug.showModal()">
        <slot/>
    </div>

    <dialog id="sug" class="modal">

        <div class="modal-box h-5/6 w-10/12 max-w-full flex flex-col">

            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                <header class="flex flex-row items-center">
                    <div>
                        <h3 class="font-bold text-2xl">Novo Pedido de Revisão</h3>
                        <p class="text-sm opacity-70">Faz duplo click no text para o alterar, ou clicka no botão "+" para adicionar novos campos!</p>
                    </div>
                </header>
                <div class="divider m-0"></div>
            </form>

            <form action="?/suggest" method="POST" on:submit={submitSuggestion}>

                <div class="mt-4">
                    <SuggestionPreview bind:ruling={changedRuling} on:valueChange={handleChange} />
                </div>

                <div class="flex mt-4">
                    <button class="btn ml-auto btn-accent btn-sm">Enviar Pedido</button>
                </div>
            </form>
        </div>
    </dialog>

</main>


