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

            <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
                <li><a href="/user">Profile</a></li>
                <li class="">
                    <form action="/logout" method="POST" class="w-full">
                        <button type="submit">
                            Logout
                        </button>
                    </form>
                </li>
            </ul>
        </div>

    </div>
</div>

<style>

    .dark-icon {
        filter: brightness(0%);
    }

</style>