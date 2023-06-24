
<script>

    import { beforeNavigate } from "$app/navigation";
    import { page } from "$app/stores";

    import { initFlash } from "sveltekit-flash-message/client";
    import { superForm } from 'sveltekit-superforms/client';

    import {switchPassword} from "$lib/scripts/passwordInputState.js";

    export let data;

    const { form, errors, enhance } = superForm(data.form);
    const flash = initFlash(page);

    let alert = true;

    beforeNavigate((nav) => {
        if ($flash && nav.from?.url.toString() !== nav.to?.url.toString()) {
            $flash = undefined;
        }
    });

</script>

<div class="flex justify-center items-center h-screen flex-col">

    <!-- Flash Message Alert -->
    {#if $flash && $flash.message && alert}

        <div class="alert alert-info w-1/3 mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>{$flash.message}</span>
            <button class="ml-auto btn btn-sm btn-ghost btn-circle" on:click={() => alert = false}>×</button>
        </div>

    {/if}

    <div class="card w-1/3 shadow-xl bg-white">

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

                <!-- Password -->
                <label for="password" class="label pt-4">
                    <span class="label-text">Insert your password</span>
                </label>
                <div class="form-control">
                    <div class="input-group">
                        <input id="password"
                               name="password"
                               type="password"
                               placeholder="Password"
                               class="input input-bordered w-full" />

                        <button type="button" class="btn btn-square btn-accent" on:click={switchPassword}>
                            <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                        </button>

                    </div>
                </div>
                {#if $errors.password}
                    <small class="text-error">{$errors.password}</small>
                {/if}

                <label class="label cursor-pointer pt-6 justify-start" for="remember">
                    <input id="remember" name="remember" type="checkbox" class="checkbox checkbox-accent checkbox-sm mr-2" />
                    <span class="text-md">Remember me</span>
                </label>
                {#if $errors.password}
                    <small class="text-error">{$errors.password}</small>
                {/if}

                <div class="pt-4">
                    <button class="btn btn-accent w-full"> Sign In</button>
                </div>

            </form>

            <!-- Want to sign up ? -->
            <p class="pt-2 text-gray-500 text-md">
                Don't have an account ? <a href="/register" class="text-accent">Sign up here</a>
            </p>

<!--            &lt;!&ndash; Continue with section &ndash;&gt;-->
<!--            <div class="divider"> Or continue with </div>-->

<!--            <div class="btn-group justify-center">-->

<!--                <ImageButton iconAlt="google-icon" iconPath="icons/google-color-icon.svg" buttonText="Google"/>-->
<!--                <ImageButton iconAlt="github-icon" iconPath="icons/facebook-color.svg" buttonText="Facebook"/>-->
<!--                <ImageButton iconAlt="github-icon" iconPath="icons/github-mark-white.svg" buttonText="GitHub"/>-->
<!--            -->
<!--            </div>-->
        </div>
    </div>
</div>