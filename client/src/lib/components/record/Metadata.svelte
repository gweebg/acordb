<script>
    export let record;

</script>

<div class="container mx-auto flex items-stretch gap-4">
    <div class="flex flex-col grow">
        <div class="grow flex mx-auto container bg-base-100 shadow-lg rounded-2xl">

            <div class="container mx-auto basis-1/4 grow px-4 py-4">
                <h2 class="px-2 py-1 font-bold text-xl">Added by:</h2>
                <p class="px-2">{record.added_by}</p>
            </div>

            <div class="divider divider-horizontal mx-0"></div>

            <div class="container mx-auto basis-1/4 grow px-4 py-4">
                <h2 class="px-2 py-1 font-bold text-xl">Added at:</h2>
                <p class="px-2">{record.added_at}</p>
            </div>

            <div class="divider divider-horizontal mx-0"></div>

            <div class="container mx-auto basis-1/4 grow px-4 py-4">
                <h2 class="px-2 py-1 font-bold text-xl">Ruling Ref:</h2>
                <p class="px-2">{record.id}</p>
            </div>
        </div>
    </div>

<!--    <div class="flex flex-col basis-20">-->
<!--        <a class="grow btn btn-accent shadow-md" href="{record.url}">-->
<!--            <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">-->
<!--                <path d="M13.0464 17C11.5404 15.4882 11.6761 12.9009 13.3494 11.2211L18.197 6.35462C19.8703 4.67483 22.4476 4.53865 23.9536 6.05046C25.4596 7.56228 25.3239 10.1496 23.6506 11.8294L21.2268 14.2626" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>-->
<!--                <path d="M16.9536 13C18.4596 14.5118 18.3239 17.0991 16.6506 18.7789L14.2268 21.2121L11.803 23.6454C10.1297 25.3252 7.55237 25.4613 6.0464 23.9495C4.54043 22.4377 4.67609 19.8504 6.34939 18.1706L8.77323 15.7373" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>-->
<!--            </svg>-->
<!--        </a>-->
<!--    </div>-->

</div>

