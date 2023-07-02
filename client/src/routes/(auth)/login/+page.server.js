import { superValidate } from 'sveltekit-superforms/server';
import { loadFlashMessage } from 'sveltekit-flash-message/server';
import { redirect } from 'sveltekit-flash-message/server';
import { PUBLIC_SERVER_API_URL } from '$env/static/public';
import { loginSchema } from "$lib/schemas/schemas.js";
import { fail } from "@sveltejs/kit";

export const load = loadFlashMessage(async (event) => {

    if (event.locals.user) {
        throw redirect(
            301,
            '/home',
            { type: "error", message: "Please sign out first before logging in!" },
            event
        );
    }

    const form = await superValidate(event, loginSchema);
    return { form };
});

export const actions = {

    default: async (event) => {

        const form = await superValidate(event, loginSchema);

        /* Validate form inputs according to zod schema. */
        if (!form.valid) {
            fail(400, { form });
            return { form };
        }

        let response;
        try {

            /* Logging in the user via the backend API. */
            response = await fetch(
            `${PUBLIC_SERVER_API_URL}/accounts/login/password/`,
            {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(form.data)
                }
            );

        } catch (err) {
            /* Handle server errors. */
            form.errors["password"] = ["There was a problem on our side, please try again later."];
            return {form};
        }

        /* Handle successful response, store access tokens in secure cookie. */
        if (response.ok) {

            const responseData = await response.json();

            let expires_in = 60 * 60 * 24 * 7;
            if (form.data.remember) expires_in = 2628000; /* If remember me is set to true, token lasts 1 month. */

            /* Setting Authorization and Refresh tokens. */
            event.cookies.set('AuthorizationToken', `Bearer ${responseData.access}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: expires_in
            });

            event.cookies.set('RefreshToken', `Refresh ${responseData.refresh}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: expires_in
            });
            

        } else {
            /* Handle sign in errors. */
            form.errors["general"] = ["Invalid username or password, try again."];
            return {form};
        }

        /* If everything went well, put the user on the homepage. */
        throw redirect(
            301,
            '/home'
        );

    }
};