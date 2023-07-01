<script>

    import { toast } from "svelte-french-toast";
    import { enhance } from "$app/forms";

    export let id;

    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    const submitSuggestion = () => {

        return async ({ result, update }) => {

            switch (result.type) {

                case "success":
                    toast.success("Suggestion made with success.", toastStyle);
                    break;

                case "invalid":
                    toast.error("Something went wrong!", toastStyle);
                    break;

                default:
                    break;

            }

            document.getElementById("sug").close();
            await update();
        }
    }

</script>

<main>

    <div onclick="sug.showModal()">
        <slot/>
    </div>

    <dialog id="sug" class="modal modal-bottom sm:modal-middle">

        <div class="modal-box w-11/12 max-w-5xl">

            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

                <header>
                    <h3 class="font-bold text-lg">New Suggestion</h3>
                    <p class="text-sm opacity-70">Click the edit button to start editing the ruling!</p>
                    <div class="divider m-0"></div>
                </header>
            </form>

            <form action="?/suggest" method="POST" use:enhance={submitSuggestion}>

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


