import {fail, redirect} from "@sveltejs/kit";
import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import { PUBLIC_SERVER_API_URL } from '$env/static/public';
import {invalidate} from "$app/navigation";
const updateSchema = z.object({

    first_name: z.string()
                .min(2, "First name has to be at least 2 characters long.")
                .max(30, "First name has to be at most 30 characters long."),

    last_name: z.string()
               .min(2, "Last name has to be at least 2 characters long.")
               .max(30, "Last name has to be at most 30 characters long."),

    password: z.string()
               .min(4, "Password has to be at least 4 character long.")
               .optional()
               .or(z.literal(''))

});


const fetchUserStats = async (authCookie) => {

    try {

        var response = await fetch(`${PUBLIC_SERVER_API_URL}/accounts/statistics/`,
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
            });

        if (response.ok) {
            return response.json();
        }
        else {
            console.log(response.status);
        }

    } catch (err) {

        /* The server is down, alert the user. */
        console.log("Server is down - ", err);
    }

}

export const load = async (event) => {

    // If user is not authenticated then we redirect him to login page.
    if (!event.locals.user || event.params.username != event.locals.user.id) {
        throw redirect(303, '/login');
    }

    const form = await superValidate(event, updateSchema);

    const authCookie = event.cookies.get('AuthorizationToken');

    if (authCookie) {
        event.locals.user.stats = await fetchUserStats(authCookie);
    }

    // If user is authenticated we return its user data to the page.
    return {user: event.locals.user, form: form};

};

export const actions = {

    genKey: async ({ cookies, locals }) => {
        
        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            try {

                var apiKeyResponse = await fetch(`${PUBLIC_SERVER_API_URL}/accounts/genAPIKey/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify({name: locals.user.email})
                    });

                if (apiKeyResponse.ok) {

                    const responseData = await apiKeyResponse.json();
                    return { success: true, data: responseData };

                }
                else {
                    console.log(apiKeyResponse.status);
                }

            } catch (err) {

                /* The server is down, alert the user. */
                console.log("Server is down - ", err);
            }
        }
    },

    update: async (event) => {

        const authCookie = event.cookies.get('AuthorizationToken');

        if (authCookie) {

            const form = await superValidate(event, updateSchema);

            /* Validate form inputs. */
            if (!form.valid) {
                fail(400, { form });
                return { form };
            }

            try {

                // Removing undefined fields since they will break the PUT request.
                Object.keys(form.data).forEach(key => form.data[key] === undefined && delete form.data[key]);

                var updateResponse = await fetch(`${PUBLIC_SERVER_API_URL}/accounts/user/${event.locals.user.id}/`,
                    {
                        method: 'PATCH',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(form.data)
                    });

                if (!updateResponse.ok) {
                    return {form};
                }

            } catch (err) {

                /* The server is down, alert the user. */
                console.log("Server is down - ", err);
            }

            throw redirect(302, '/user');
        }

    },

    setAdmin: async ({ cookies, request }) => {

        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            const data = await request.formData();
            const userId = data.get('id');

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_SERVER_API_URL}/accounts/makeadmin/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify({email: userId})
                    }
                );

            } catch (err) {
                return {
                    success: false,
                    message: "There is a problem on our side, please try again later."
                }
            }

            if (!response.ok) {
                return {
                    success: false,
                    message: "The user does not exist."
                }
            }

            return {
                success: true
            }

        }
    }
};