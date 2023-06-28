<script>

    import { toast } from "svelte-french-toast";
    import { enhance } from "$app/forms";

    export let id;

    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    const submitFavorite = () => {

        return async ({ result, update }) => {

            switch (result.type) {

                case "success":
                    toast.success("Added to favorites!", toastStyle);
                    break;

                case "invalid":
                    toast.error("Could not add to favorites!", toastStyle);
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

    <div onclick="fav.showModal()">
        <slot/>
    </div>

    <dialog id="fav" class="modal modal-bottom sm:modal-middle">

        <div class="modal-box">

            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                <header>
                    <h3 class="font-bold text-lg">Save to Favorites</h3>
                    <p class="text-sm opacity-70">Provide a description to save the ruling in your favorites.</p>
                    <div class="divider m-0"></div>
                </header>
            </form>

            <form action="?/favorite" method="POST" use:enhance={submitFavorite}>

                <input type="text" class="hidden" name="id" value={id}>

                <textarea
                        name="description"
                        placeholder="Enter a description"
                        class="textarea textarea-bordered textarea-md w-full mt-4 mb-0" ></textarea>

                <div class="modal-action">
                    <button class="btn btn-sm btn-accent">
                        Save
                    </button>
                </div>
            </form>

        </div>
    </dialog>

</main>


