<script>

    import { superForm } from 'sveltekit-superforms/client';
    import {switchPassword} from "$lib/scripts/passwordInputState.js";

    import { enhance } from "$app/forms";
	import { PUBLIC_GOOGLE_CLIENT_ID } from '$env/static/public';

    export let data;
    const { form, errors } = superForm(data.form);

    let buttonContent = "Registar";
    let loading = false;

    const submitHandler = () => {

        loading = true;
        buttonContent = "A criar conta..."

        return async ({ update}) => {
            await update();
            loading = false;
            buttonContent = "Registar"
        }
    }

</script>

<svelte:head>
    <script src="https://accounts.google.com/gsi/client" async defer></script>
    <title>
        Acordb - Registar conta
    </title>
</svelte:head>

<!-- Centering content -->
<div class="flex justify-center items-center h-screen flex-col">

    <!-- Base card -->
    <div class="card w-1/3 shadow-xl bg-white">

        <!-- Card Header (Logo) -->
        <div class="flex justify-center">
            <a href="/home">
                <img class="w-40 h-30 pt-4" src="logo-textless.svg" alt="logo"/>
            </a>
        </div>

        <!-- Card Body (Title, Form, Sign In Button, Continue With) -->
        <div class="card-body">

            <h1 class="text-center gap-2 text-3xl font-semibold leading-7">Criar conta em Acordb</h1>

            <!-- Card Body and Form -->
            <form action="?/signup" method="POST" class="pt-4" use:enhance={submitHandler}>

                <!-- First/Last Names -->
                <div class="flex flex-row flex-grow gap-2">

                    <div class="w-full">
                        <label class="label" for="first_name">
                            <span id="first_name" class="label-text">Primeiro Nome</span>
                        </label>
                        <input disabled={loading} name="first_name" type="text" placeholder="Primeiro Nome" class="input input-bordered w-full" bind:value={$form.first_name}/>
                    </div>

                    <div class="w-full">
                        <label class="label" for="last_name">
                            <span id="last_name" class="label-text">Ultimo Nome</span>
                        </label>
                        <input disabled={loading} name="last_name" type="text" placeholder="Ultimo Nome" class="input input-bordered w-full" bind:value={$form.last_name}/>
                    </div>

                </div>

                {#if $errors.first_name || $errors.last_name}
                    <small class="text-error">{$errors.first_name}</small>
                    <small class="text-error">{$errors.last_name}</small>
                {/if}

                <!-- Email -->
                <label class="label pt-4" for="email">
                    <span id="email" class="label-text">Insira o seu endereço de email</span>
                </label>
                <input
                        name="email"
                        type="text"
                        placeholder="Email"
                        class="input input-bordered w-full"
                        disabled={loading}
                        bind:value={$form.email}
                />
                {#if $errors.email}
                    <small class="text-error">{$errors.email}</small>
                {/if}

                <!-- Filiation -->
                <label class="label pt-4" for="filiation">
                    <span id="filiation" class="label-text">Filiação (opcional)</span>
                </label>
                <input
                        name="filiation"
                        type="text"
                        placeholder="Filiação"
                        class="input input-bordered w-full"
                        bind:value={$form.filiation}
                        disabled={loading}
                />

                <!-- Password -->
                <label for="password" class="label">
                    <span class="label-text">Insira a password</span>
                </label>
                <div class="form-control">
                    <div class="input-group">
                        <input id="password"
                               name="password"
                               type="password"
                               placeholder="Password"
                               class="input input-bordered w-full"
                               disabled={loading}
                        />

                        <button id="passwordIconBtn" type="button" class="btn btn-square btn-secondary" on:click={switchPassword}>
                            <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                        </button>

                    </div>
                </div>

                <!-- Terms of Service -->
                <label for="tos" class="label cursor-pointer pt-6 justify-start">
                    <input id="tos" name="tos" type="checkbox" class="checkbox checkbox-primary checkbox-sm mr-2" bind:value={$form.tos}/>
                    <span class="text-md">Aceito os termos e condições <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="text-secondary">Termos e condições</a></span>
                </label>
                {#if $errors.tos}
                    <small class="text-error">{$errors.tos}</small>
                {/if}

                <button class="btn btn-primary w-full" disabled={loading}>
                    {buttonContent}
                </button>

            </form>

            <p class="pt-2 text-gray-500 text-md">
                Já tem uma conta ? <a href="/login" class="text-secondary">Entre Aqui</a>
            </p>
            <div class="flex justify-center">
                <div id="g_id_onload"
                     data-client_id="{PUBLIC_GOOGLE_CLIENT_ID}"
                     data-ux_mode="redirect"
                     data-login_uri="http://localhost/api/login/google">
                </div>
                <div class="g_id_signin" data-type="standard"></div>
            </div>

        </div>
    </div>
</div>