import { redirect } from 'sveltekit-flash-message/server';
import { loadFlashMessage } from 'sveltekit-flash-message/server';

import { PUBLIC_API_URL } from '$env/static/public';
import { error } from "@sveltejs/kit";

export const load = loadFlashMessage(async (event) => {

    // If user is not authenticated then we redirect him to login page.
    if (!event.locals.user || event.params.username != event.locals.user.id) {
        throw redirect(303, '/login');
    }

    const authCookie = event.cookies.get('AuthorizationToken');
    let favorites;

    if (authCookie) {
       favorites = await fetchFavorites(authCookie);
    }

    return {
        user: event.locals.user,
        data: favorites
    };

});

const fetchFavorites = async (authCookie) => {

    try {

        const response = await fetch(`${PUBLIC_API_URL}/favorites/`,
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
            });

        if (response.ok) return response.json();
        else console.log(response.status);

    } catch (err) { throw error(500, "Server is down."); }

}

export const actions = {

    delete: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await event.request.formData();

            let response;
            try {

                response = await fetch(
                `${PUBLIC_API_URL}/favorites/${data.get('id')}/`,
                {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                    }
                );

            } catch (err) {
                throw error(500, "Server is down.");
            }

            if (response.ok) {
                throw redirect(
                    { type: "success", message: "Successfully deleted favorite!" },
                    event
                )
            }

            else {
                throw redirect(
                    { type: "error", message: "Could not delete the bookmark." },
                    event
                )
            }
        }
    },

    edit: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await event.request.formData();

            const putData = {
                id: data.get('id'),
                acordao: data.get('process'),
                description: data.get('description')
            };

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_API_URL}/favorites/${data.get('id')}/`,
                {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(putData)
                    }
                );

            } catch (err) {
                throw error(500, "Server is down.");
            }


            if (response.ok) {
                throw redirect(
                    { type: "success", message: "Successfully edited!" },
                    event
                )
            }

            else {
                throw redirect(
                    { type: "error", message: "Something went wrong, try again!" },
                    event
                )
            }
        }
    }
};