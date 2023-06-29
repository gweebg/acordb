import { fetchRuling } from "$lib/scripts/fetchRuling.js";
import { fail } from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";


const fetchFavorite = async (rulingId, cookie) => {

    let response;
    try {

        response = await fetch(
            `${PUBLIC_API_URL}/favorites/isFavorite/${rulingId}/`,
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': cookie },
            }
        );

    } catch (err) { throw new Error(err); }

    return response.status === 200;

}

export async function load({ params, locals, cookies }) {


    const auth = cookies.get('AuthorizationToken');

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    return {
        user: user
    };
}

export const actions = {

    favorite: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await event.request.formData();
            console.log(data);

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_API_URL}/favorites/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify({
                            acordao: data.get('id'),
                            description: data.get('description')
                        })
                    });

            } catch (err) {
                console.log("Servidor em baixo");
                return fail(500, "Server is down.");
            }

            if (!response.ok) {
                const data = await response.json();
                return fail(400, data.toString());
            }
        }
    }
};