import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import { fail, redirect } from "@sveltejs/kit";
import { PUBLIC_API_URL } from '$env/static/public';
const loginSchema = z.object({

    username: z.string().email({message: "Invalid email address."}),
    password: z.string({
        required_error: "Please fill in the password field.",
        invalid_type_error: "Password must be a string."
      }).min(1),
    remember: z.boolean()

});

export const load = async (event) => {

    if (event.locals.user) {
        throw redirect(301, '/home');
    }

    const form = await superValidate(event, loginSchema);
    return { form };
};

export const actions = {

    /* Default is local password login. */
    default: async (event) => {

        const form = await superValidate(event, loginSchema);

        /* Validate form inputs. */
        if (!form.valid) {
            fail(400, { form });
            return { form };
        }

        let response;

        try {

            /* Logging in the user via the backend API. */
            response = await fetch(`${PUBLIC_API_URL}/accounts/login/password/`,
            {
                method: 'POST', 
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(form.data)
            });

        } catch (err) {

            /* The server is down, alert the user. */
            console.log("Error -", err);
            form.errors["password"] = ["There was a problem on our side, please try again later."];
            return {form};

        }

        /* Handle successful response, store access tokens in secure cookie. */
        if (response.ok) {

            const responseData = await response.json();

            if (form.data.remember) responseData.expires_in = 2628000; /* If remember me is set to true, token lasts 1 month. */

            event.cookies.set('AuthorizationToken', `Bearer ${responseData.access_token}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: responseData.expires_in
            });

            event.cookies.set('RefreshToken', `Refresh ${responseData.refresh_token}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: responseData.expires_in
            });
            

        } else {

            form.errors["password"] = ["Invalid username or password, try again."];
            return {form};

        }

        /* If everything went well, put the user on the homepage. */
        throw redirect(302, '/');

    }
};