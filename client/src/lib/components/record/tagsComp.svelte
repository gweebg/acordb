<script lang="ts">
    export let tags: Array<string>;
</script>

{#each tags as t}
    <span class="badge badge-info badge-lg">{t}</span>
{/each}