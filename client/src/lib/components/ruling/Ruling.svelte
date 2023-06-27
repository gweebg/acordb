<script>

    import RulingHeader from "$lib/components/ruling/RulingHeader.svelte";
    import RulingDetails from "$lib/components/ruling/RulingDetails.svelte";

    export let ruling; /* TODO */

    const headerData = {
        process: "1371/15.0T8VRL.G1-A.S1",
        added_by: "admin@admin.pt",
        added_at: "22 Jun 2023"
    }

    const bodyData = {
        court: "Supremo Tribunal de Justiça",
        rapporteur: "Guilherme Geraldes Sampaio",
        ruling_date: "13 Jul 2002",
        descriptors: [
            "Despacho",
            "Contrato de Crédito ao Consumo",
            "Formalidade Ad Probationem",
            "Liberdade de Imprensa",
            "Prova de Celebração do Contrato",
            "Prova da Convenção Sobre a Taxa de Juros"
        ],
        text: "O direito ao bom nome e reputação consiste essencialmente no direito a não ser ofendido ou lesado na sua honra\n" +
            "                    , dignidade ou consideração social mediante imputação feita por outrem, bem como no direito a defender-se dessa\n" +
            "                    ofensa e a obter a competente reparação. No direito à honra haverá que distinguir diferentes esferas ou círculos, sendo\n" +
            "                    a geral reportada ao nível pessoa, familiar, honestidade, rectidão, ou ligada diretamente à dignidade humana, mas a par\n" +
            "                    desta há a invariável, liga."
    }

</script>


<main class="w-full">

    <div class="card bg-base-100 shadow-xl">

        <div class="card-body">

            <RulingHeader rulingData={headerData}/>

            <div class="divider my-0"></div>

            <RulingDetails rulingData={bodyData}/>

            <div class="card-actions justify-end">
                <a href="/" class="btn btn-accent btn-sm">View More</a>
            </div>

        </div>
    </div>

</main>