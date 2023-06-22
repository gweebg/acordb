<script>
    import Navbar from "$lib/components/home/Navbar.svelte";
    import GeneralSection from "$lib/components/new/GeneralSection.svelte";
    import {inputs, process, url, tags, body} from "$lib/stores/form.js";

    import jsonToFormData from '@ajoelp/json-to-formdata';
    import ContentSection from "$lib/components/new/ContentSection.svelte";
    import ReviewSection from "$lib/components/new/ReviewSection.svelte";
    import Footer from "$lib/components/Footer.svelte";

    export let data;

    let sections = { general: true, content: false, details: false };
    let buttonContent = "Next";
    let isDisabled = true;

    const nextSection = () => {

        if (sections.general === true && sections.content === true) {

            const button = document.getElementById('submit');

            sections.details = true;
            buttonContent = "Finish";

            button.addEventListener('click', function() {
                button.setAttribute('type', 'submit');
            });

        }
        else if (sections.general === true) {
            sections.content = true;
            isDisabled = false;
        }
    }

    const prevSection = () => {

        if (sections.details && sections.content && sections.general) {
            sections.details = false;
        } else if (sections.general && sections.content && !sections.details) {
            sections.content = false;
            isDisabled = true;
        }

        const button = document.getElementById('submit');
        button.addEventListener('click', function() {
            button.setAttribute('type', 'button');
        });

        buttonContent = "Next";
    }

    const handleSubmit = async (event) => {

        event.preventDefault();

        let data = {
            fields: undefined,
            process: "",
            tags: [],
            url: "",
            body: undefined
        };

        const unsubFields = inputs.subscribe(
            fieldList => data.fields = fieldList
        );

        const unsubProcess = process.subscribe(
            processId => data.process = processId
        );

        const unsubTags = tags.subscribe(
            tagList => data.tags = tagList
        );

        const unsubUrl = url.subscribe(
            url => data.url = url
        );

        const unsubBody = body.subscribe(
            obj => data.body = obj
        );

        const formData = jsonToFormData(data);

        await fetch('?/new', {
            method: 'POST',
            body: formData
        });

        unsubFields(); unsubProcess(); unsubTags(); unsubUrl(); unsubBody();
    }

</script>


<div>

    <Navbar isAuthenticated={data.user.is_administrator}/>

    <!-- New judgment form. -->
    <div class="px-4 mb-[100px] mt-[80px] mx-48">

        <header>
            <h2 class="text-3xl font-bold">Add a new ruling!</h2>
            <p class="opacity-50">Pay attention to what fields are obligatory!</p>
            <div class="divider"></div>
        </header>

        <form class="flex justify-center flex-col" id="new" action="?/new" method="POST" on:submit={handleSubmit}>

            <!-- Steps -->
            <ul class="steps">
                <li class="step {sections.general ? 'step-primary' : ''}">General Information</li>
                <li class="step {sections.content ? 'step-primary' : ''}">Content</li>
                <li class="step {sections.details ? 'step-primary' : ''}">Review & Submit</li>
            </ul>

            <!-- Form Content -->
            <div>
                {#if sections.details === true}

                    <ReviewSection/>

                {:else if sections.content === true}

                    <ContentSection/>

                {:else}

                    <GeneralSection fields={data.fields}/>
                    
                {/if}
            </div>

            <!-- Next/Submit Button -->
            <div class="ml-auto">
                <button id="back" disabled='{isDisabled}' type="button" class="btn" on:click={prevSection}>Back</button>
                <button id="submit" class="btn btn-primary" type="button" on:click={nextSection}>{buttonContent}</button>
            </div>

        </form>

    </div>

    <Footer/>

</div>





