import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import { fail, redirect } from "@sveltejs/kit";

const loginSchema = z.object({

    username: z.string().email({message: "Invalid email address"}),
    password: z.string().min(1),
    remember: z.boolean()

});

export const load = async (event) => {

    const form = await superValidate(event, loginSchema);
    return { form };
};

export const actions = {

    default: async (event) => {

        const form = await superValidate(event, loginSchema);

        /* Validate form inputs. */
        if (!form.valid) {
            fail(400, { form });
            return { form };
        }

        try {

            /* Logging in the user via the backend API. */
            var response = await fetch("http://127.0.0.1:8000/accounts/login/", 
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

        /* Handle succssesfull response, store access tokens in secure cookir. */
        if (response.ok) {

            const responseData = await response.json();

            if (responseData.access_token === undefined) {

                form.errors["password"] = ["Invalid username or password, try again."];
                return {form};

            }

            if (form.data.remember) responseData.expires_in = 2628000; /* If remember me is set to true, token lasts 1 month. */

            event.cookies.set('AuthorizationToken', `Bearer ${responseData.access_token}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: responseData.expires_in
            });

            event.cookies.set('RefreshTken', `Refresh ${responseData.refresh_token}`, {
                httpOnly: true,
                path: '/',
                secure: true,
                sameSite: 'strict',
                maxAge: responseData.expires_in
            });

        } else return { form };

        /* If everything went well, put the user on the homepage. */
        throw redirect(302, '/');

    }
};