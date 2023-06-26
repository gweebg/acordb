<script>

    import { superForm } from 'sveltekit-superforms/client';
    import {switchPassword} from "$lib/scripts/passwordInputState.js";

    import { enhance } from "$app/forms";

    export let data;
    const { form, errors } = superForm(data.form);

    let buttonContent = "Sign Up";
    let loading = false;

    const submitHandler = () => {

        loading = true;
        buttonContent = "Creating Account..."

        return async ({ update}) => {
            await update();
            loading = false;
            buttonContent = "Sign Up"
        }
    }

</script>

<!-- Centering content -->
<div class="flex justify-center items-center h-screen flex-col">

    <!-- Base card -->
    <div class="card w-1/3 shadow-x bg-white">

        <!-- Card Header (Logo) -->
        <div class="flex justify-center">
            <a href="/home">
                <img class="w-40 h-30 pt-4" src="logo-textless.svg" alt="logo"/>
            </a>
        </div>

        <!-- Card Body (Title, Form, Sign In Button, Continue With) -->
        <div class="card-body">

            <h1 class="text-center gap-2 text-3xl font-semibold leading-7">Sign up to Acordb</h1>

            <!-- Card Body and Form -->
            <form action="?/signup" method="POST" class="pt-4" use:enhance={submitHandler}>

                <!-- First/Last Names -->
                <div class="flex flex-row flex-grow gap-2">

                    <div class="w-full">
                        <label class="label" for="first_name">
                            <span id="first_name" class="label-text">First name</span>
                        </label>
                        <input disabled={loading} name="first_name" type="text" placeholder="First name" class="input input-bordered w-full" bind:value={$form.first_name}/>
                    </div>

                    <div class="w-full">
                        <label class="label" for="last_name">
                            <span id="last_name" class="label-text">Last name</span>
                        </label>
                        <input disabled={loading} name="last_name" type="text" placeholder="Last name" class="input input-bordered w-full" bind:value={$form.last_name}/>
                    </div>

                </div>

                {#if $errors.first_name || $errors.last_name}
                    <small class="text-error">{$errors.first_name}</small>
                    <small class="text-error">{$errors.last_name}</small>
                {/if}

                <!-- Email -->
                <label class="label pt-4" for="email">
                    <span id="email" class="label-text">Insert your address</span>
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
                    <span id="filiation" class="label-text">Filiation (optional)</span>
                </label>
                <input
                        name="filiation"
                        type="text"
                        placeholder="Filiation"
                        class="input input-bordered w-full"
                        bind:value={$form.filiation}
                        disabled={loading}
                />

                <!-- Password -->
                <label for="password" class="label">
                    <span class="label-text">State your password</span>
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

                        <button type="button" class="btn btn-square btn-accent" disabled={loading} on:click={switchPassword}>
                            <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                        </button>

                    </div>
                </div>

                <!-- Terms of Service -->
                <label for="tos" class="label cursor-pointer pt-6 justify-start">
                    <input id="tos" name="tos" type="checkbox" class="checkbox checkbox-accent checkbox-sm mr-2" bind:value={$form.tos}/>
                    <span class="text-md">I accept the <a href="/" class="text-accent">Terms and Conditions</a></span>
                </label>
                {#if $errors.tos}
                    <small class="text-error">{$errors.tos}</small>
                {/if}

                <button class="btn btn-accent w-full" disabled={loading}>
                    {buttonContent}
                </button>

            </form>

            <p class="pt-2 text-gray-500 text-md">
                Already have an account ? <a href="/login" class="text-accent">Login here</a>
            </p>

        </div>
    </div>
</div>