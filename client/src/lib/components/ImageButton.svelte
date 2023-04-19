<script>

    export let iconPath;
    export let iconAlt;
    export let buttonText;

</script>


<button class="btn flex justify-center items-center" on:click>
    <img class="w-auto h-5 pr-2" src={iconPath} alt={iconAlt}>
    <span class="pt-1">{buttonText}</span>
</button>

