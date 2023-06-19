<script>

    import { enhance } from '$app/forms';

    export let favData;
    export let auth;

    let isEditing = false;
    let currPath = "/icons/edit.svg";
    let description = favData.description;

    const editMode = () => {

        if (isEditing === true) {
            isEditing = false;
            currPath = "/icons/edit.svg";
        }

        else {
            isEditing = true;
            currPath = "/icons/book.svg";
        }
    }
    
</script>


<div class="modal-box">

    <!-- Header -->
    <div class="flex flex-row items-center">

        <!-- Title -->
        <h2 class="text-xl">Process {favData.processo} <span class="opacity-40">#{favData.id}</span></h2>

        <!-- Controls -->
        <div class="ml-auto flex flex-row gap-1">

            <!-- Edit Button -->
            <button class="btn btn-accent btn-sm" on:click={editMode}>
                <img src={currPath} alt="Edit">
            </button>

            <!-- Delete Button -->
            <form action="?/delete" method="POST">
                <input type="text" name="id" class="hidden" value={favData.id}>
                <input type="text" name="process" class="hidden" value={favData.processo}>
                <button class="btn btn-error btn-sm">
                    <img src="/icons/delete.svg" alt="Delete">
                </button>
            </form>

        </div>

    </div>

    <div class="divider"></div>

    <!-- Body -->
    {#if !isEditing}

        {#if favData.description.length === 0}
            <p class="opacity-40">No description available.</p>
        {:else}
            <p>{favData.description}</p>
        {/if}

        <div class="modal-action">
            <label for={favData.id} class="btn btn-sm">Close</label>
        </div>

    {:else}

        <form action="?/edit" method="POST">

            <input type="text" name="id" class="hidden" value={favData.id}>
            <input type="text" name="process" class="hidden" value={favData.processo}>
            <textarea
                    id="description"
                    name="description"
                    placeholder="Type a new description"
                    bind:value={description}
                    class="textarea textarea-accent w-full"></textarea>

            <div class="modal-action">
                <button class="btn btn-accent btn-sm">Save</button>
                <label for={favData.id} class="btn btn-sm">Close</label>
            </div>

        </form>

    {/if}

</div>