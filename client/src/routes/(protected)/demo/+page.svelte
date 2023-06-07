<script>
    /** @type {import('./$types').PageData} */
    export let data;

</script>

<h1>Protected Route!</h1>

<form action="/logout" method="POST">
    <button type="submit" class="btn btn-primary">Logout</button>
</form>