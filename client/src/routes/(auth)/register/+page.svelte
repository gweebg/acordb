<script>


</script>

<div class="flex justify-center items-center h-screen">

    <div class="card w-1/3 shadow-xl">

        <div class="card-body">

            <!-- Card Header -->
            <div class="flex justify-center items-center">

                <img
                        class="w-8 h-8 mr-2"
                        src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
                        alt="logo"
                />
                Acordb

            </div>
            <h2 class="text-center gap-2 text-xl font-semibold leading-7">Create an Account</h2>

            <!-- Card Body and Form -->
            <form action="" class="pt-4">

                <label class="label">
                    <span class="label-text">Choose a username</span>
                </label>
                <input type="text" placeholder="Username" class="input input-bordered input-primary w-full"/>

                <label class="label pt-4">
                    <span class="label-text">Your address</span>
                </label>
                <input type="text" placeholder="example@service.domain" class="input input-bordered input-primary w-full"/>

                <label class="label pt-4">
                    <span class="label-text">Your password</span>
                </label>
                <input type="password" placeholder="Password" class="input input-bordered input-primary w-full"/>

                <label class="label pt-4">
                    <span class="label-text">Repeat your password</span>
                </label>
                <input type="password" placeholder="Repeat the Password" class="input input-bordered input-primary w-full"/>

                <label class="label cursor-pointer pt-6 justify-start">
                    <input type="checkbox" checked="checked" class="checkbox checkbox-primary checkbox-sm mr-2" />
                    <span class="text-md">I accept the <a href="#" class="text-primary">Terms and Conditions</a></span>
                </label>

                <div class="pt-4">
                    <button class="btn btn-primary w-full"> Sign Up</button>
                </div>

            </form>

            <p class="pt-2 text-gray-500 text-md">
                Already have an account ? <a href="/login" class="text-primary">Login here</a>
            </p>

        </div>
    </div>

</div>