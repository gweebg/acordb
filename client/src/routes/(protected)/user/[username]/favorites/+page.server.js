import {redirect} from "@sveltejs/kit";

export const load = async (event) => {

    // If user is not authenticated then we redirect him to login page.
    if (!event.locals.user || event.params.username != event.locals.user.id) {
        throw redirect(303, '/login');
    }

    const authCookie = event.cookies.get('AuthorizationToken');

    if (authCookie) {
       var favorites = await fetchFavorites(authCookie);
    }

    // If user is authenticated we return its user data to the page.
    return {user: event.locals.user, data: favorites, token: authCookie};

};

const fetchFavorites = async (authCookie) => {

    try {

        var response = await fetch("http://127.0.0.1:8000/favorites/",
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
            });

        if (response.ok) return response.json();
        else console.log(response.status);

    } catch (err) { console.log("Server is down - ", err); }

}