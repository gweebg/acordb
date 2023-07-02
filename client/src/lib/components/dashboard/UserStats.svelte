<script>
    import {convertDate} from "$lib/scripts/dateConvert.js";

    export let user;
</script>

<div class="flex gap-4 flex-wrap">

    <div class="stats shadow overflow-x-hidden">

        <div class="stat">
            <div class="stat-title">Conta criada em</div>
            <div class="stat-value">{convertDate(user.stats.Criação)}</div>
        </div>

    </div>

    {#if !user.is_administrator}

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Tu fizeste</div>
                <div class="stat-value">{user.stats.Changes}</div>
                <div class="stat-desc">pedidos de revisão!</div>
            </div>
        </div>

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Foram <span class="text-success">aceites</span> </div>
                <div class="stat-value">{user.stats.ChangesAccepted}</div>
                <div class="stat-desc">pedidos de revisão.</div>
            </div>
        </div>

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Foram <span class="text-error">rejeitados</span></div>
                <div class="stat-value">{user.stats.ChangesDenied}</div>
                <div class="stat-desc"> pedidos de alteração</div>
            </div>
        </div>

    {:else}

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Tu criaste</div>
                <div class="stat-value">{user.stats["Acordãos"]}</div>
                <div class="stat-desc">novo(s) acórdão(s)!</div>
            </div>
        </div>

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Tu reviste</div>
                <div class="stat-value">{user.stats["Reviews"]}</div>
                <div class="stat-desc">acórdãos!</div>
            </div>
        </div>

    {/if}

    <div class="stats shadow">
        <div class="stat">
            <div class="stat-title">Total de Favoritos</div>
            <div class="stat-value">{user.stats.Favoritos}</div>
        </div>
    </div>

</div>