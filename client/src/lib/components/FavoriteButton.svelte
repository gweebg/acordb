<script>

    import { toast } from "svelte-french-toast";
    import { enhance } from "$app/forms";

    export let id;
    export let isDisabled;

    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    const submitFavorite = () => {

        return async ({ result, update }) => {

            switch (result.type) {

                case "success":
                    toast.success("Adicionado aos favoritos!", toastStyle);
                    break;

                case "invalid":
                    toast.error("Não foi possível adicionar aos favoritos!", toastStyle);
                    break;

                default:
                    break;

            }

            document.getElementById("fav").close();
            await update();
        }
    }

</script>

<main>

    {#if !isDisabled}

        <div onclick="fav.showModal()">
            <slot/>
        </div>

    {:else}

        <div>
            <slot/>
        </div>

    {/if}

    <dialog id="fav" class="modal modal-bottom sm:modal-middle">

        <div class="modal-box">

            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                <header>
                    <h3 class="font-bold text-lg">Guardar nos Favoritos</h3>
                    <p class="text-sm opacity-70">Podes especificiar uma descrição para te localizares melhor!</p>
                    <div class="divider m-0"></div>
                </header>
            </form>

            <form action="?/favorite" method="POST" use:enhance={submitFavorite}>

                <input type="text" class="hidden" name="id" value={id}>

                <textarea
                        name="description"
                        placeholder="Adiciona uma descrição"
                        class="textarea textarea-bordered textarea-md w-full mt-4 mb-0" ></textarea>

                <div class="modal-action">
                    <button class="btn btn-sm btn-accent">
                        Guardar
                    </button>
                </div>
            </form>

        </div>
    </dialog>

</main>


