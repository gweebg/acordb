<script>

    export let favData;

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
        <h2 class="text-xl">Favorite <span class="opacity-40">#{favData.id}</span></h2>

        <!-- Controls -->
        <div class="ml-auto flex flex-row gap-1">

            <!-- Edit Button -->
            <button class="btn btn-accent btn-sm px-0 btn-circle" on:click={editMode}>
                <img src={currPath} alt="Edit">
            </button>

            <!-- Delete Button -->
            <form action="?/delete" method="POST">
                <input type="text" name="id" class="hidden" value={favData.id}>
                <input type="text" name="process" class="hidden" value={favData.acordao}>
                <button class="btn btn-error btn-sm px-0 btn-circle">
                    <img src="/icons/delete.svg" alt="Delete">
                </button>
            </form>

        </div>

    </div>

    <p class="opacity-50">Ref: {favData.acordao}</p>


    <div class="divider mt-0"></div>

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
            <input type="text" name="process" class="hidden" value={favData.acordao}>
            <textarea
                    id="description"
                    name="description"
                    placeholder="Type a new description"
                    bind:value={description}
                    class="textarea textarea-accent w-full"></textarea>

            <div class="modal-action">
                <button class="btn btn-accent btn-sm mt-2">Save</button>
                <label for={favData.id} class="btn btn-sm mt-2">Close</label>
            </div>

        </form>

    {/if}

</div>