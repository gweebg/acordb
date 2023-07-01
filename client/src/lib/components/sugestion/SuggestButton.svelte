<script>

    import { toast } from "svelte-french-toast";
    import { enhance } from "$app/forms";
    import SuggestionPreview from "$lib/components/sugestion/SuggestionPreview.svelte";

    export let ruling;

    let changedRuling = ruling;

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
                        <h3 class="font-bold text-2xl">New Suggestion</h3>
                        <p class="text-sm opacity-70">Click on the text to change any field or add more fields with the "+" button at the bottom.</p>
                    </div>
                </header>
                <div class="divider m-0"></div>
            </form>

            <div class="mt-4">
                <SuggestionPreview bind:ruling={changedRuling} on:valueChange={handleChange} />
            </div>

        </div>
    </dialog>

</main>


