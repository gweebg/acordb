<script>

    import {onMount} from "svelte";
    import {PUBLIC_API_URL} from "$env/static/public";


    const calculateAvg = (list) => {
        return list.reduce((a, b) => a + b, 0) / list.length;
    }

    const date = new Date().toUTCString();

    let stats = {
        Processo: "-",
        Processos24horas: "-",
        RecordsMes: [0],
        Administradores: "-",
        Cosumidores: "-"
    };

    const fetchStatistics = async () => {

        try {

            const response = await fetch(`${PUBLIC_API_URL}/statistics/`,
                {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' },
                });

            if (response.ok) {
                stats = await response.json();
            }
            else {
                console.log(`[Error ${response.status}] fetchStatistics @ fetchStatistics`);
            }

        } catch (err) {console.log(`[Error] fetchStatistics @ fetchStatistics ${err}`);}

    }

    onMount(async () => await fetchStatistics());

</script>


<div id="stats" class="px-4 my-[100px] mx-48">



    <div class="flex justify-between">

        <h2 class="text-3xl font-bold">Estatísticas do Serviço</h2>

        <small class="opacity-40">Atualizado em {date} </small>

    </div>


    <div class="opacity-60">
        <p>Nesta área podes ver algumas estatísticas gerais sobre o Acordb.</p>
    </div>

    <div class="divider"></div>

    <div class="flex justify-center">

        <div class="stats shadow">

            <div class="stat">
                <div class="stat-figure text-primary">
                    <img src="/icons/stats/file.svg" alt="file">
                </div>
                <div class="stat-title">#Acórdãos Totais</div>
                <div class="stat-value text-accent">{stats.Processos}</div>
            </div>

            <div class="stat">
                <div class="stat-figure text-primary">
                    <img src="/icons/stats/clock.svg" alt="clock">
                </div>
                <div class="stat-title">#Acórdãos Totais (Últimas 24H)</div>
                <div class="stat-value text-accent">{stats.Processos24horas}</div>
            </div>

            <div class="stat">
                <div class="stat-figure text-primary">
                    <img src="/icons/stats/avg.svg" alt="avg">
                </div>
                <div class="stat-title">#Acórdãos Médios por Mês</div>
                <div class="stat-value text-accent">{calculateAvg(stats.RecordsMes)}</div>
            </div>

            <div class="stat">
                <div class="stat-figure text-primary">
                    <img src="/icons/stats/admins.svg" alt="admin">
                </div>
                <div class="stat-title">Total de Administradores</div>
                <div class="stat-value text-accent">{stats.Administradores}</div>
            </div>

            <div class="stat">
                <div class="stat-figure text-primary">
                    <img src="/icons/stats/user.svg" alt="users">
                </div>
                <div class="stat-title">Total de Consumidores</div>
                <div class="stat-value text-accent">{stats.Consumidores}</div>
            </div>

        </div>

    </div>

</div>