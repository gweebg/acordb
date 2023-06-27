<script>

    import {convertDate} from "$lib/scripts/dateConvert.js";

    export let rulingData;

</script>

<main>

    <header class="flex flex-row items-center">
        <div class="">
            <h2 class="card-title">Process no. {rulingData.process}</h2>
        </div>

        <div class="ml-auto opacity-50">
            <p>{rulingData.added_by}</p>
            <p class="text-right">{convertDate(rulingData.added_at)}</p>
        </div>
    </header>

</main>
