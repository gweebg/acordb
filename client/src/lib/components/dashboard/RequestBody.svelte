<script>

    import {compareRulings} from "$lib/scripts/jsonDiff.js";
    import {onMount} from "svelte";

    export let content = {};

    let diffHTML = '';

    onMount(() => {
        const originalString = {
            Processo: "P123-321",
            Descritores: ["MIN", "MAX"],
            "Texto Integral": "Isto é um texto gigante xd, tenho de meter o word wrap no pre, não me posso esquecer! Tenho de me lembrar, agora estou apenas a spammar chars para garantir que da trigger hahahaa."
        };
        const modifiedString = {
            Processo: "P123-321",
            Descritores: ["MIN", "MAX"],
            "Texto Integral": "Isto é um texto pequeno xD, tenho de meter o word wrap no pre, não me posso esquecer!! Tenho de me lembrar, agora estou apenas a spammar chars para garantir que da trigger hahahaa.",
            Data: "22 Jun 2023",
            Data: "22 Jun 2023",
        };
        diffHTML = compareRulings(originalString, modifiedString);
    });

</script>


<main>

    <div class="divider mt-0"></div>
    <header class="flex flex-row mt-4">
        <h1 class="text-lg">Viewing differences between original and requested:</h1>
        <div class="ml-auto">
            <div class="badge badge-accent">
                Added
            </div>

            <div class="ml-2 badge badge-warning">
                Removed
            </div>
        </div>
    </header>

    <!-- Diff Viewer    -->
    <div class="flex flex-row my-4">

        <div class="scroll-container w-full mx-2 p-2 bg-base-100 rounded-xl max-h-[800px] overflow-y-scroll p-4">

            <header class="flex flex-row mb-4 items-center">



            </header>

            <div>
                {@html diffHTML}
            </div>
        </div>
    </div>

    <form action="default" method="POST">
        <div class="flex items-center">

            <a href="/" class="text-xs opacity-80 underline">See ruling details</a>

            <div class="ml-auto">
                <button class="btn btn-sm btn-error">Deny</button>
                <button class="btn btn-sm btn-accent">Accept</button>
            </div>

        </div>
    </form>

</main>