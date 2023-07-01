<script>

    import {toast, Toaster} from "svelte-french-toast";
    import {enhance} from "$app/forms";

    export let form = {};


    const toastStyle = {
        style: 'border: 1px solid #2dbcab; background-color: #e4e9ec;',
        position: "bottom-right",
        duration: 5000
    };

    const close = () => {
        document.getElementById("setAdmin").close();
        form = undefined;
    }

    const submit = ({ data, cancel }) => {

        const { id } = Object.fromEntries(data);
        if (id.length <= 0) {
            form = {success: false, message: "This field is mandatory."}
            cancel();
        }

        return async ({ update }) => {
            await update();
        }
    }

</script>

<main>

    <Toaster/>

    <!-- You can open the modal using ID.showModal() method -->
    <button
            class="btn btn-accent mt-4"
            onclick="setAdmin.showModal()">
        Add Administrator
    </button>

    <dialog id="setAdmin" class="modal">

        <div class="modal-box">

            <button on:click={close} class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

            <header>
                <h3 class="font-bold text-lg">Create New Administrator!</h3>
                <p class="opacity-50">Type in the email of the user to turn into an admin.</p>
                <div class="divider mt-0"></div>
            </header>

            <form action="?/setAdmin" method="POST" use:enhance={submit}>
                <input name="id" type="text" placeholder="User identification" class="input input-bordered input-accent w-full" />
                {#if form?.success === false}
                    <small class="text-error">{form?.message}</small>
                {/if}

                <div class="flex flex-row mt-4">
                    <button class="btn btn-sm btn-accent ml-auto">Add</button>
                </div>
            </form>

        </div>
    </dialog>

</main>