import {redirect} from "@sveltejs/kit";
import { PUBLIC_API_URL } from '$env/static/public';
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

        var response = await fetch(`${PUBLIC_API_URL}/favorites/`,
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
            });

        if (response.ok) return response.json();
        else console.log(response.status);

    } catch (err) { console.log("Server is down - ", err); }

}

export const actions = {

    delete: async ({ cookies, request, locals }) => {

        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await request.formData();

            try {

                var response = await fetch(`${PUBLIC_API_URL}/favorites/${data.get('id')}/`,
                    {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                    });

                if (!response.ok) {
                    console.log(response.status);
                }

            } catch (err) {

                /* The server is down, alert the user. */
                console.log("Server is down - ", err);
            }

            throw redirect(301, `/user/${locals.user.id}/favorites`);
        }
    },

    edit: async ({ cookies, request}) => {

        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await request.formData();

            const putData = {
                id: data.get('id'),
                processo: data.get('process'),
                description: data.get('description')
            };

            try {

                var response = await fetch(`${PUBLIC_API_URL}/favorites/${data.get('id')}/`,
                    {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(putData)
                    });

                if (!response.ok) {
                    console.log(response.status);
                }

            } catch (err) {

                /* The server is down, alert the user. */
                console.log("Server is down - ", err);
            }
        }
    }
};