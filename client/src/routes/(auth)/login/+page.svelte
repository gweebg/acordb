
<script>

    import ImageButton from "$lib/components/ImageButton.svelte";

    import { superForm } from 'sveltekit-superforms/client';
    import { GoogleAuth, FacebookAuth } from '@beyonk/svelte-social-auth'

    export let data;
    const { form, errors, enhance } = superForm(data.form);

    const GOOGLE_CLIENT_ID = "316555827922-thlb7qjblpqovk9033h29ub4rejimaqd.apps.googleusercontent.com";

    const handleGoogleSignIn = (/** @type {any} */ event) => {
        console.log(event);
    };

</script>

<div class="flex justify-center items-center h-screen flex-col">

    <div class="card w-1/3 shadow-xl">

        <!-- Card Header (Logo) -->
        <div class="flex justify-center">
            <a href="/home">
                <img class="w-40 h-30 pt-4" src="logo-textless.svg" alt="logo"/>
            </a>
        </div>

        <!-- Card Body (Title, Form, Sign In Button, Continue With)-->
        <div class="card-body">

            <!-- Title -->
            <h1 class="text-text_base text-center gap-2 text-3xl font-semibold leading-7">Sign into Acordb</h1>

            <!-- Card Body and Form -->
            <form method="POST" class="pt-4" use:enhance>

                <label class="label" for="username">
                    <span class="label-text">Insert your email</span>
                </label>
                <input id="username" name="username" type="text" placeholder="Username" class="input input-bordered w-full" bind:value={$form.username}/>
                {#if $errors.username}
                    <small class="text-error">{$errors.username}</small>
                {/if}

                <label class="label pt-4" for="password">
                    <span class="label-text">Insert your password</span>
                </label>
                <input id="password" name="password" type="password" placeholder="Your password" class="input input-bordered w-full"/>
            
                <label class="label cursor-pointer pt-6 justify-start" for="remember">
                    <input id="remember" name="remember" type="checkbox" class="checkbox checkbox-primary checkbox-sm mr-2" />
                    <span class="text-md">Remember me</span>
                </label>
                {#if $errors.password}
                    <small class="text-error">{$errors.password}</small>
                {/if}

                <div class="pt-4">
                    <button class="btn btn-primary w-full"> Sign In</button>
                </div>

            </form>

            <!-- Want to sign up ? -->
            <p class="pt-2 text-gray-500 text-md">
                Don't have an account ? <a href="/register" class="text-primary">Sign up here</a>
            </p>

            <!-- Continue with section -->
            <div class="divider"> Or continue with </div>

            <div class="btn-group justify-center">
                

                <GoogleAuth clientId={GOOGLE_CLIENT_ID} on:auth-success={e => console.dir(e.detail.user)}>
                    <ImageButton iconAlt="google-icon" iconPath="icons/google-color-icon.svg" buttonText="Google"/>
                </GoogleAuth>

                <ImageButton iconAlt="github-icon" iconPath="icons/facebook-color.svg" buttonText="Facebook"/>
                <ImageButton iconAlt="github-icon" iconPath="icons/github-mark-white.svg" buttonText="GitHub"/>
            
            </div>
        </div>
    </div>
</div>