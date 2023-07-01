<script>

</script>


<div id="search" class="px-4 mb-[100px] mt-[80px] mx-48">

    <div class="flex justify-between">

        <h2 class="text-3xl font-bold">Advanced Search</h2>

        <!-- modal button -->
        <label for="help-modal" class="btn btn-sm btn-circle btn-accent modal-button">?</label>
        <!-- modal content -->
        <input type="checkbox" id="help-modal" class="modal-toggle">
        <div class="modal">
            <div class="modal-box">
                <h2 class="text-xl">Search Terms:</h2>
                <div class="modal-action">
                    <label for="help-modal" class="btn">Close</label>
                </div>
            </div>
        </div>

    </div>

    <div class="opacity-60">
        <p>In the area you can search any ruling by the parameters bellow.</p>
    </div>

    <div class="divider"></div>

    <form action="/search" method="POST">

        <div class="flex flex-col gap-4">

            <div class="form-control">

                <div class="input-group justify-center">
                    <input id="input" type="text" placeholder="Search for a term" class="input input-bordered w-full" />
                    <select class="select select-bordered ">
                        <option selected>Ruling Title</option>
                        <option>Ruling Text</option>
                    </select>
                </div>

                <div class="flex flex-row gap-2 pt-4">

                    <select class="select select-bordered">
                        <option disabled selected>Jurisdiction</option>
                        <option>Ruling Text</option>
                    </select>

                    <select class="select select-bordered">
                        <option disabled selected>Neutral Citation</option>
                        <option>Ruling Text</option>
                    </select>


                    <select class="select select-bordered">
                        <option disabled selected>Judge</option>
                        <option>Ruling Text</option>
                    </select>

                    <select class="select select-bordered">
                        <option disabled selected>From Date</option>
                        <option>Ruling Text</option>
                    </select>

                    <select class="select select-bordered">
                        <option disabled selected>To Date</option>
                        <option>Ruling Text</option>
                    </select>

                </div>
            </div>


            <button class="btn btn-accent gap-2 text-md w-full">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                Search
            </button>

        </div>


    </form>

    <!-- <button class="btn" on:load={advanced_search_modal.showModal()}>open modal</button>
        <dialog id="advanced_search_modal" class="modal">
        <form method="dialog" class="modal-box h-5/6 w-10/12 max-h-full max-w-full p-0 flex flex-col overflow-hidden">
            <div class="basis-12 bg-primary flex justify-between items-center h-12">
                <h3 class="text-primary-content font-bold text-xl pl-4">Pesquisa Avancada:</h3>
                <button class="w-1/12 btn btn-accent rounded-none focus-visible:outline-none h-full flex flex-row justify-center items-center">close</button>
            </div>
            <div class="flex w-full h-[calc(100%-3em)]">
                <div class="flex flex-col basis-1/2 overflow-hidden">
                    <div class="px-8 mt-8">
                        <span>
                            <h2 class="inline text-3xl font-bold align-middle">Campos</h2>
                            <p class="inline text-lg align-middle">- Selecione o campo pelo qual pretende pesquisar</p>
                        </span>
                        <div class="divider mb-0"></div>
                    </div>
                    <div class="flex flex-wrap gap-8 p-8 overflow-y-auto">
                        {#each ["juiz", "alo", "alo", "alo", "alo", "alo", "alo", "alo", "alo", "alo"] as campo}
                        <div class="basis-1/3 grow">
                            <div class="card bg-card-accent shadow-lg min-h-full">
                                <div class="card-body">
                                    <h2 class="px-1 card-title">campo</h2>
                                    <p class="break-all">bla</p>
                                </div>
                            </div>
                        </div>
                        {/each}
                    </div>
                </div>
                <div class="flex flex-col basis-1/2 overflow-hidden">

                </div>
            </div>
        </form>
        <form method="dialog" class="modal-backdrop">
            <button>close</button>
        </form>
    </dialog> -->
</div>