import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import {fail, redirect} from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";

const registerSchema = z.object({

    first_name: z.string().min(3),
    last_name: z.string().min(3),
    email: z.string().email(),
    filiation: z.string(),
    password: z.string().min(1),
    tos: z.boolean()

});

export const load = async (event) => {

    const form = await superValidate(event, registerSchema);
    return { form };
};

export const actions = {

    signup: async (event) => {

        const form = await superValidate(event, registerSchema);

        /* Assert the TOS are checked. */
        if (form.data.tos === false) {
            form.errors["tos"] = ["You must accept the Terms of Service to create an account."];
            form.valid = false;
        }

        if (!form.valid) {
            fail(400, { form });
        }

        let response;

        try {

            delete form.data.tos;

            /* Logging in the user via the backend API. */
            response = await fetch(`${PUBLIC_API_URL}/accounts/user/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(form.data)
                });

        } catch (err) {

            /* The server is down, alert the user. */
            form.errors["password"] = ["There was a problem on our side, please try again later."];
            return {form};

        }

        /* Handle errors and redirect to login page! */
        const responseData = await response.json();
        if (!response.ok) {

            console.log(responseData);
            if (responseData.email) form.errors["email"] = responseData.email
            return {form};

        }

        /* If everything went well, put the user on the homepage. */
        throw redirect(302, '/login');

    }

};