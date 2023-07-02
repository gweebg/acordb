<script>

    import SideBar from "$lib/components/dashboard/SideBar.svelte";
    import UserStats from "$lib/components/dashboard/UserStats.svelte";

    import {enhance} from '$app/forms';
    import {superForm} from "sveltekit-superforms/client";
    import {switchPassword} from "$lib/scripts/passwordInputState.js";
    import SetAdmin from "$lib/components/dashboard/SetAdmin.svelte";


    export let data; // Data returned from the load function at +page.server.js
    export let form; // Data returned from the form genKey.

    const { errors } = superForm(data.form);

    let visible = true;

    let originalData = {
        first_name: data.user.first_name,
        last_name: data.user.last_name
    }

    let firstName = data.user.first_name;
    let lastName = data.user.last_name;


    const resetForm = () => {
        firstName = originalData.first_name;
        lastName = originalData.last_name;
    }

    const copyToClipboard = () => {

        const clipContent = (element) => {
            navigator.clipboard.writeText(element.value.toString());
        };

        clipContent(document.getElementById('api_key'));
    }

</script>

<svelte:head>
    <title>
        Acordb - Perfil
    </title>
</svelte:head>

<div class="flex flex-row">

    <div class="fixed">
        <SideBar
            active={{profile: true, rulings: false, favourites: false, settings: false, requests: false}}
            name={data.user.email}
            basePath={"/user/" + data.user.id}
            isAdmin={data.user.is_administrator}
        />
    </div>

    <!-- Content -->
    <div class="flex-1 h-screen p-12 overflow-y-auto ml-96">

        <!-- Header -->
        <header>

            <div class="text-sm breadcrumbs">
                <ul>
                    <li><p>Dashboard</p></li>
                    <li><p>Perfil</p></li>
                </ul>
            </div>


            <h2 class="text-3xl font-bold">Perfil de {data.user.first_name}</h2>
            <div class="divider"></div>

        </header>

        <!-- Content -->
        <div class="flex flex-row">

            <!-- Account -->
            <div class="w-1/2 mr-12">

                <h3 class="text-xl font-bold pb-4">A Tua Conta</h3>

                <form method="POST" action="?/update">

                    <label for="email" class="label">
                        <span class="label-text">Endereço de Email</span>
                    </label>
                    <input id="email"
                           name="email"
                           disabled
                           type="text"
                           value={data.user.email}
                           class="input input-bordered w-full" />

                    <div class="flex flex-row gap-2">

                        <div class="flex-1">
                            <label for="first_name" class="label">
                                <span class="label-text">Primeiro Nome</span>
                            </label>
                            <input id="first_name"
                                   name="first_name"
                                   type="text"
                                   bind:value={firstName}
                                   class="input input-bordered w-full" />
                        </div>

                        <div class="flex-1">
                            <label for="last_name" class="label">
                                <span class="label-text">Último Nome</span>
                            </label>
                            <input id="last_name"
                                   name="last_name"
                                   type="text"
                                   bind:value={lastName}
                                   class="input input-bordered w-full" />
                        </div>
                    </div>

                    <label for="password" class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <div class="form-control">
                        <div class="input-group">
                            <input id="password"
                                   name="password"
                                   type="password"
                                   placeholder="Escreve uma nova password"
                                   class="input input-bordered w-full" />

                            <button type="button" class="btn btn-square btn-accent" on:click={switchPassword}>
                                <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                            </button>

                        </div>
                    </div>


                    <div class="mt-6 flex flex-row justify-between">

                        <div>
                            {#if $errors.first_name}
                                <p class="text-error text-sm">{$errors.first_name}</p>
                            {/if}
                            {#if $errors.last_name}
                                <p class="text-error text-sm">{$errors.last_name}</p>
                            {/if}
                            {#if $errors.password}
                                <p class="text-error text-sm">{$errors.password}</p>
                            {/if}
                        </div>

                        <fieldset>
                            <button type="button" class="btn" on:click={resetForm}>Limpar</button>
                            <button class="btn btn-accent">Guardar Alterações</button>
                        </fieldset>

                    </div>

                </form>

            </div>

            <!-- Stats -->
            <div class="w-1/2">
                <h3 class="text-xl font-bold pb-4">As Tuas Estatísticas</h3>
                <UserStats user={data.user}/>
            </div>

        </div>


        <!-- API Key -->
        <div class="mt-4">

            <div class="divider"></div>

            <!-- Header -->
            <header>
                <h3 class="text-xl font-bold pb-4">Gerar Chave de API</h3>

                <p>
                    Por favor guarda este segredo algures seguro e acessível. Devido a questões de segurança
                    <strong>não poderás voltar a ver a chave</strong> através desta área.
                </p>

                <p>Caso percas a chave, terás de gerar uma nova!</p>
            </header>

            <!-- Form -->
            <div class="mt-4">

                <form method="POST" action="?/genKey" use:enhance on:submit={() => visible = !visible}>

                    {#if visible}

                        <button class="btn btn-accent">Gerar API Key</button>

                    {/if}

                </form>

                {#if form?.success}

                    <div class="form-control">
                        <div class="input-group">

                            <input id="api_key"
                                   readonly
                                   value={form?.data.key}
                                   class="input input-bordered w-full" />

                            <button type="button" on:click={copyToClipboard} class="btn btn-square btn-accent">
                                <img id="copy" src="/icons/profile/copy.svg" alt="Eye">
                            </button>

                        </div>
                    </div>

                {/if}

                {#if !visible && form && !form.success}
                    <p class="text-error">Something went wrong, try again later.</p>
                {/if}

                {#if !visible && !form}
                    <p class="btn btn-ghost text-md loading">Loading</p>
                {/if}

            </div>

        </div>


        {#if data.user.is_administrator}
            <!-- Make Admin -->
            <div class="mt-4">

                <div class="divider"></div>

                <!-- Header -->
                <header>
                    <h3 class="text-xl font-bold pb-4">Transformar Utilizador em Administrador</h3>
                    <p>Preenche o formulário abaixo com o email do utilizador.</p>
                </header>

                <SetAdmin/>

            </div>
        {/if}

    </div>
</div>