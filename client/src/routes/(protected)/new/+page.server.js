import {error, fail, redirect} from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";


export const load = async ({ locals }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user) {
        throw redirect(303, '/login');
    }

    // If the user is authenticated but is a consumer, block the access.
    if (locals.user.is_administrator === false) {
        throw error(404, { message: "You don't have the privilege to access this endpoint." });
    }

    /*
    const fieldsResponse = await fetch(
        `${PUBLIC_API_URL}/acordaos/fields/`,
        {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }

        });

    if (fieldsResponse.ok) {

        const responseData = await userResponse.json();

        // This is dumb, at this point just = responseData.
        event.locals.user = {
            id: responseData.id,
            email: responseData.email,
            first_name: responseData.first_name,
            last_name: responseData.last_name,
            filiation: responseData.filiation,
            is_administrator: responseData.is_administrator
        };

    }
    else {
        console.log(userResponse.status);
    }
    */


    return {user: locals.user, fields: ["Acordãos", "Contencioso", "Votação", "Requerido", "Data"]};

};

export const actions = {

    new: async ({ cookies, locals, request }) => {

        const data = await request.formData();
        console.log(data);

    }
};