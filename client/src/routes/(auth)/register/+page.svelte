<script>


</script>

<!-- Centering content -->
<div class="flex justify-center items-center h-screen flex-col">

    <!-- Base card -->
    <div class="card w-1/3 shadow-xl">

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
            <form method="POST" class="pt-4">

                <label class="label" for="username">
                    <span id="username" class="label-text">Choose a username</span>
                </label>
                <input type="text" placeholder="Username" class="input input-bordered w-full"/>

                <label class="label pt-4" for="email">
                    <span id="email" class="label-text">Insert your address</span>
                </label>
                <input type="text" placeholder="example@service.domain" class="input input-bordered w-full"/>

                <label class="label pt-4" for="password">
                    <span id="password" class="label-text">State your password</span>
                </label>
                <input type="password" placeholder="Password" class="input input-bordered w-full"/>

                <label class="label cursor-pointer pt-6 justify-start">
                    <input type="checkbox" class="checkbox checkbox-primary checkbox-sm mr-2" />
                    <span class="text-md">I accept the <a href="/tos" class="text-primary">Terms and Conditions</a></span>
                </label>

                <div class="pt-4">
                    <button class="btn btn-primary w-full" type="submit"> Sign Up</button>
                </div>

            </form>

            <p class="pt-2 text-gray-500 text-md">
                Already have an account ? <a href="/login" class="text-primary">Login here</a>
            </p>

        </div>
    </div>
</div>