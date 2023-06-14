<script lang="ts">
    export let title: string;
    export let text: string;
</script>

<div class="basis-1/5 grow">
    <div class="card bg-card-accent shadow-lg min-h-full">
        <div class="card-body">
            <h2 class=" px-1 card-title">{title}</h2>
            <p class="break-all">{text}</p>
        </div>
    </div>
</div>