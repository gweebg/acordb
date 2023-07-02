<script>

    import {newForm} from "$lib/stores/form.js";

</script>


<main class="bg-white rounded-xl my-4 p-6">

    <!-- Title -->
    <header>
        <h2 class="text-2xl font-bold">Ruling Content</h2>
        <p class="opacity-50">Here you can specify the ruling decision, summary and integral text.</p>
        <div class="divider mt-0"></div>
    </header>

    <!-- Inputs -->
    <div class="mb-2">

        <!-- Decision -->
        <div class="form-control">
            <label class="label" for="decision">
                <span class="label-text">Ruling Decision</span>
            </label>
            <textarea
                    bind:value={$newForm.body.decision}
                    id="decision"
                    class="textarea textarea-bordered h-24"
                    placeholder="Here you can specify the decision that the court ruled for the ruling"></textarea>
        </div>


        <!-- Summary -->
        <div class="form-control">
            <label class="label" for="summary">
                <span class="label-text">Summary</span>
            </label>
            <textarea
                    bind:value={$newForm.body.summary}
                    id="summary"
                    class="textarea textarea-bordered h-24"
                    placeholder="Here you can specify the summary for the ruling"></textarea>
        </div>

        <!-- Summary -->
        <div class="form-control">
            <label class="label" for="text">
                <span class="label-text">Integral Text</span>
            </label>
            <textarea
                    bind:value={$newForm.body.text}
                    id="text"
                    class="textarea textarea-bordered h-24"
                    placeholder="Here you can specify the full content of the ruling"></textarea>
        </div>

    </div>


    <small class="text-warning pt-4">(!) Note that none of the above fields are mandatory.</small>
</main>