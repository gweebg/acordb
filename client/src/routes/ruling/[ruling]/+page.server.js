import { fetchRuling } from "$lib/scripts/fetchRuling.js";
import { fail } from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";


export async function load({ params, locals }) {

    const ruling = await fetchRuling(params.ruling);

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    return {
        ruling: ruling,
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

            } catch (err) { throw fail(500, "Server is down."); }

            if (!response.ok) {
                const data = await response.json();
                throw fail(400, data.toString());
            }
        }
    }
};