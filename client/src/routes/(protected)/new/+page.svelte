<script>
    import Navbar from "$lib/components/home/Navbar.svelte";
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

</script>


<div>

    <Navbar isAuthenticated={data.user.is_administrator}/>

    <!-- New judgment form. -->
    <div class="px-4 mb-[100px] mt-[80px] mx-48">


        <h2 class="text-3xl font-bold">Add a new ruling!</h2>
        <p class="opacity-50">Pay attention to what fields are obligatory!</p>
        <div class="divider"></div>

        <form class="flex justify-center flex-col" id="new" action="?/new" method="POST">

            <!-- Steps -->
            <ul class="steps">
                <li class="step {sections.general ? 'step-primary' : ''}">General Information</li>
                <li class="step {sections.content ? 'step-primary' : ''}">Content</li>
                <li class="step {sections.details ? 'step-primary' : ''}">Details</li>
            </ul>

            <!-- Form Content -->
            <div>

                {#if sections.details === true}

                    <p>Details</p>

                {:else if sections.content === true}

                    <p>Content</p>

                {:else}

                    <p>General</p>
                    
                {/if}


            </div>

            <!-- Next/Submit Button -->
            <div class="ml-auto">
                <button id="back" disabled='{isDisabled}' type="button" class="btn" on:click={prevSection}>Back</button>
                <button id="submit" class="btn btn-accent" type="button" on:click={nextSection}>{buttonContent}</button>
            </div>

        </form>

    </div>

    <Footer/>

</div>





