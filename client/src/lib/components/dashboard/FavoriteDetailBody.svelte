<script>

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

    const save = () => {


    }

</script>


<div class="modal-box">

    <div class="flex flex-row items-center">

        <h2 class="text-xl">Process {favData.processo} <span class="opacity-40">#{favData.id}</span></h2>

        <div class="ml-auto">

            <button class="btn btn-accent btn-sm" on:click={editMode}>
                <img src={currPath} alt="Edit">
            </button>
            <button class="btn btn-error btn-sm">
                <img src="/icons/delete.svg" alt="Delete">
            </button>

        </div>

    </div>

    <div class="divider"></div>

    {#if !isEditing}

        <p>{favData.description}</p>

    {:else}

        <textarea
                placeholder="Type a new description"
                bind:value={description}
                class="textarea textarea-accent w-full"></textarea>

    {/if}

    <div class="modal-action">

        {#if isEditing}
            <button class="btn btn-accent btn-sm" on:click={save}>Save</button>
        {/if}

        <label for={favData.id} class="btn btn-sm">Close</label>
    </div>


</div>