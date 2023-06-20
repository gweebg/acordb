<script>
    import {convertDate} from "$lib/scripts/dateConvert.js";

    export let user;
</script>

<div class="flex gap-4 flex-wrap">

    <div class="stats shadow overflow-x-hidden">

        <div class="stat">
            <div class="stat-title">Created at</div>
            <div class="stat-value">{convertDate(user.stats.Criação)}</div>
            <div class="stat-desc">Account creation date</div>
        </div>

    </div>

    {#if !user.is_administrator}

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">You have made</div>
                <div class="stat-value">{user.stats.Changes}</div>
                <div class="stat-desc">requests</div>
            </div>
        </div>

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">You have</div>
                <div class="stat-value">{user.stats.ChangesAccepted}</div>
                <div class="stat-desc"><span class="text-accent">accepted</span> change requests.</div>
            </div>
        </div>

        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">You have</div>
                <div class="stat-value">{user.stats.ChangesDenied}</div>
                <div class="stat-desc"><span class="text-error">denied</span> change requests.</div>
            </div>
        </div>
    {/if}

    <div class="stats shadow">
        <div class="stat">
            <div class="stat-title">Favorites</div>
            <div class="stat-value">{user.stats.Favoritos}</div>
        </div>
    </div>

</div>