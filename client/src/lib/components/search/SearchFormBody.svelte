<script>

    import { searchForm } from "$lib/stores/search.js";
    import {goto, invalidate} from "$app/navigation";

    import Select from "svelte-select";

    import DescriptorInput from "$lib/components/search/DescriptorInput.svelte";

    export let fields = []

    const newField = () => {

        searchForm.update(form => {

            const id = form.fields.length;
            return {
                ...form,
                fields: [...form.fields, { id: id, value: { field: '', value: '' } }]
            }

        });

    }

    const removeField = (id) => {

        searchForm.update(form => {
            const fields = form.fields.filter(input => input.id !== id);
            return {
                ...form,
                fields: fields
            }
        });

    }

    const updateField = (id, field) => {


        searchForm.update(form => {

            let fields = form.fields;

            fields = fields.map(item => {
                if (item.id === id) return { ...item, value: { value: item.value.value, field: field.label } }
                return item;
            })

            return {
                ...form,
                fields: fields
            }

        });

    };

    const handleSearch = async (event) => {

        event.preventDefault();

        let data = {
            tags: [],
            from_date: "",
            to_date: ""
        };

        const unsubscribe = searchForm.subscribe(
            formData => {

                const {fields, tags, from_date, to_date } = formData;

                for (const field in Object.keys(fields)) {
                    data[fields[field].value.field.value] = fields[field].value.value;
                }

                data.tags = tags;
                data.from_date = from_date;
                data.to_date = to_date;

            }
        );

        unsubscribe();

        let queryString = "";

        for (const field in data) {

            if (field === "tags") {
                data.tags.forEach(tag => {
                    queryString += `tags[]=${tag}&`;
                })
            }

            else if (data[field] !== ""){
                queryString += `${field}=${data[field]}&`
            }
        }

        queryString = queryString.slice(0, -1); //encodeURIComponent(queryString.toString())
        await goto("/search?" + queryString);
        window.location.reload();
    }

</script>

<main data-sveltekit-reload>

    <form action="?/search" method="POST" on:submit={handleSearch}>

        <div class="flex flex-row items-center mb-2">

            <div class="w-1/2 mr-4">
                <div class="form-control w-full">
                    <label class="label">
                        <span class="label-text">Search By Tags</span>
                    </label>
                    <DescriptorInput bind:tags={$searchForm.tags}/>
                </div>
            </div>

            <div class="flex flex-row w-1/2 flex-grow gap-2">
                <div class="form-control w-full">
                    <label class="label">
                        <span class="label-text">Search From Date</span>
                    </label>
                    <input type="date" class="input input-bordered w-full" bind:value={$searchForm.from_date}>
                </div>

                <div class="form-control w-full">
                    <label class="label">
                        <span class="label-text">Search To Date</span>
                    </label>
                    <input type="date" class="input input-bordered w-full" bind:value={$searchForm.to_date}>
                </div>
            </div>

        </div>


        {#each $searchForm.fields as input (input.id)}

            <div class="flex items-center">

                <div class="flex flex-row gap-2 my-2 w-full">
                    <div class="join w-full">

                        <div class="join-item">
                            <Select
                                    items={fields}
                                    placeholder="Select a field"
                                    --width="300px"
                                    --border-radius="0.5rem 0 0 0.5rem"
                                    --height="48px"
                                    --background="#e4e9ec"
                                    bind:value={input.value.field}
                                    on:change={() => updateField(input.id, input.value.field)}
                            />
                        </div>

                        <div class="flex-grow mr-4">
                            <div>
                                <input
                                        class="input input-bordered join-item w-full"
                                        placeholder="Field value"
                                        bind:value={input.value.value}
                                />
                            </div>
                        </div>

                    </div>
                </div>

                <button type="button" class="btn btn-circle btn-xs ml-auto" on:click={() => removeField(input.id)}>
                    <img src="/icons/cross.svg" alt="delete">
                </button>

            </div>

        {/each}

        <button type="button" class="btn btn-sm w-full mb-4 text-2xl" on:click={newField}>
            +
        </button>

        <button class="btn btn-accent w-full">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
            Search
        </button>

    </form>

</main>
