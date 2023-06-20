<script lang="ts">
    export let tags: Array<string>;

</script>

<div class="flex gap-2 flex-wrap">
    {#each tags as t}
        <span class="badge badge-info badge-lg">{t}</span>
    {/each}
</div>
