<script>

    import RequestBody from "$lib/components/dashboard/RequestBody.svelte";

    import {convertDate} from "$lib/scripts/dateConvert.js";

    export let details;
    export let isAdmin;

    const date = new Date().toDateString();

    const getStatusColor = (status) => {

        if (status === "pending") return "badge-error";
        else return "badge-accent";

    }

</script>

<div class="collapse collapse-arrow bg-base-200">

    <!-- Hidden input for controls. -->
    <input type="radio" name="my-accordion-2" checked="checked" />

    <!-- Collapse Title   -->
    <div class="collapse-title text-xl font-medium">
        <div class="flex gap-2 items-center">

            <div class="flex flex-col">
                <div class="flex flex-row gap-2 items-center">
                    <div class="badge {getStatusColor(details.status)} badge-md"></div>
                    <p>Pedido de Revisão de Acórdão</p>
                </div>

                <small class="opacity-50 text-xs">Feito por {details.sujested_by}</small>
            </div>

            <div class="ml-auto flex-row flex">
                <div class="badge mr-2">
                    {convertDate(details.added_at)}
                </div>

                {#if details.reviewer}
                    <div class="badge">
                        Revisto por {details.reviewer}
                    </div>
                {/if}
            </div>

        </div>
    </div>

    {#if details.status === "pending"}
        <div class="collapse-content">
            <RequestBody details={details} {isAdmin}/>
        </div>
    {:else}
        <div class="collapse-content">
            <div class="divider mt-0"></div>
            <div class="flex flex-row items-center">
                <p>Revisto em: {date}</p>
                <a href={"/ruling/" + details.acordao} class="btn btn-accent btn-sm ml-auto">Abrir</a>
            </div>
        </div>
    {/if}

</div>