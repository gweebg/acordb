import { loadFlashMessage } from 'sveltekit-flash-message/server';
import { superValidate } from 'sveltekit-superforms/server';
import { redirect } from "sveltekit-flash-message/server";

import { fail } from "@sveltejs/kit";

import { PUBLIC_API_URL } from "$env/static/public";
import { accountSchema } from "$lib/schemas/schemas.js";


export const load = loadFlashMessage(async (event) => {
    const form = await superValidate(event, accountSchema);
    return { form };
});

export const actions = {

    signup: async (event) => {

        const form = await superValidate(event, accountSchema);

        /* Handle the not acceptance of the terms of service. */
        if (form.data["tos"] === false) {
            form.errors["tos"] = ["You must accept the Terms of Service to create an account."];
            form.valid = false;
        }

        if (!form.valid) fail(400, { form });

        let response;
        try {

            delete form.data["tos"]; /* Deleting the unnecessary key. */

            /* Registering the account via the backend API. */
            response = await fetch(
                `${PUBLIC_API_URL}/accounts/user/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(form.data)
                }
            );

        } catch (err) {
            /* Handle other server erros (server being down). */
            form.errors["password"] = ["There was a problem on our side, please try again later."];
            return {form};
        }

        /* Handle possible errors given from the data API. */
        const responseData = await response.json();
        if (!response.ok) {
            if (responseData.email) form.errors["email"] = responseData.email
            return {form};
        }

        /* Once the user creates the account, it is redirected to the login page to continue. */
        throw redirect(
            302,
            '/login',
            { type: "success", message: "Account created with success, please log in to continue!" },
            event
        );
    }
};