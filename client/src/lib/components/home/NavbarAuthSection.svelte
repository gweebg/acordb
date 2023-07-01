<script>

    export let isAdmin;

</script>

<div class="flex gap-4 items-center">

    <!-- Dashboard Button -->
    <a
        class="btn btn-ghost gap-2 text-left justify-start items-center text-base-100-focus"
        href="/user">
        Dashboard
    </a>

    {#if isAdmin}

        <!-- Add New Button -->
        <a
            class="btn btn-ghost gap-2 text-left justify-start items-center text-base-100-focus"
            href="/new">
            New
        </a>

    {/if}

    <div class="dropdown dropdown-end">

        <div class="dropdown dropdown-hover">
            <label tabindex="0" class="btn btn-ghost avatar">
                <div class="w-10 rounded-full">
                    <img src="/icons/navbar/avatar.svg" />
                </div>
            </label>

            <form action="/logout" method="POST" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
                <li class="h-8 mb-2 w-full flex items-center justify-center">
                    <a href="/user" class="w-full flex justify-center">Profile</a>
                </li>
                <li class="h-8 w-full flex items-center justify-center">
                    <button type="submit" class="w-full h-full flex justify-center">
                        Logout
                    </button>
                </li>
            </form>
        </div>

    </div>
</div>

<style>

    .dark-icon {
        filter: brightness(0%);
    }

</style>