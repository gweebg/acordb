<script>

    import RequestBody from "$lib/components/dashboard/RequestBody.svelte";

    export let details = {};

</script>

<div class="collapse collapse-arrow bg-base-200">

    <!-- Hidden input for controls. -->
    <input type="radio" name="my-accordion-2" checked="checked" />

    <!-- Collapse Title   -->
    <div class="collapse-title text-xl font-medium">
        <div class="flex gap-2 items-center">

            <div class="flex flex-col">
                <div class="flex flex-row gap-2 items-center">
                    <div class="badge badge-accent badge-md"></div>
                    <p>Change request for ruling <span class="font-semibold">P91-124</span></p>
                </div>

                <small class="opacity-50 text-xs">Requested by Guilherme Sampaio</small>
            </div>

            <div class="ml-auto flex-row flex">
                <div class="badge mr-2">
                    22 Jun 2023
                </div>

                <div class="badge">
                    JTCA
                </div>
            </div>

        </div>
    </div>

    <div class="collapse-content">
        <RequestBody/>
    </div>

</div>