<script>

    import RulingHeader from "$lib/components/ruling/RulingHeader.svelte";
    import RulingDetails from "$lib/components/ruling/RulingDetails.svelte";
    import { checkValue } from "$lib/scripts/utils.js";

    export let ruling;
    export let isRecord = false;

    const { id, added_by, added_at, acordao, tags, data } = ruling;

    const headerData = {
        process: checkValue(data.Processo),
        added_by: checkValue(added_by),
        added_at: checkValue(added_at)
    }

    const bodyData = {
        court: checkValue(data.tribunal),
        rapporteur: checkValue(data.Relator),
        ruling_date: checkValue(data["Data da Decisão"]),
        descriptors: tags,
        text: checkValue(data["Texto Integral"])
    }

    const redirectToRuling = () => {
        if (isRecord)
            window.location.href = `/record/${id}`;
        else
            window.location.href = `/ruling/${acordao}`;
    }

</script>


<main class="w-full my-4">

    <div class="card bg-base-100 shadow-lg transition ease-in-out delay-150
                hover:-translate-y-1 hover:cursor-pointer hover:bg-card-hover hover:shadow-xl duration-300  border-accent hover:border-[1px]"
         on:click={redirectToRuling}>

        <div class="card-body">

            <RulingHeader rulingData={headerData}/>

            <div class="divider my-0"></div>

            <RulingDetails rulingData={bodyData}/>

        </div>
    </div>

</main>