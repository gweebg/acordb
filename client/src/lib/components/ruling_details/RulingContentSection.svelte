<script>

    import {checkValue} from "$lib/scripts/utils.js";

    export let field;
    export let value;

</script>

<main class="mb-12 whitespace-normal">
    <p class="text-xl font-bold">{field}</p>
    <div class="divider m-0"></div>
    <p class="opacity-70 break-words">{checkValue(value)}</p>
</main>