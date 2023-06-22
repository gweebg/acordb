import {error, fail, redirect} from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";
import {convert} from "$lib/scripts/formdataToJson.js";


export const load = async ({ locals }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user) {
        throw redirect(303, '/login');
    }

    // If the user is authenticated but is a consumer, block the access.
    if (locals.user.is_administrator === false) {
        throw error(404, { message: "You don't have the privilege to access this endpoint." });
    }

    let fields = await fetchFields();
    return {user: locals.user, fields: fields};

};

export const actions = {

    new: async ({ cookies, locals, request }) => {

        let data = await request.formData(); /* This holds the form data, un-formatted because of black magic. */
        let final = convert(data); /* This holds the form data, formatted as readable JSON. */

        /* TODO: Make POST request to API to add new ruling. */

    }
};

const fetchFields = async () => {

    const fieldsResponse = await fetch(
        `${PUBLIC_API_URL}/acordaos/fields/`,
        {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }

        });

    if (fieldsResponse.ok) {

        /* This data is in the format [{name:"..."},{name:"..."},...] */
        const responseData = await fieldsResponse.json();

        /* Reserved fields that are already put out for the user to fill in. */
        const reservedFields = ['url', 'Processo', 'Descritores', 'Texto Integral', 'Sumário', 'Decisão']

        /* Return the flattened list with the reserved fields removed. */
        return responseData
            .map((value) => { return value.name})
            .filter((value) => {
                return !reservedFields.includes(value);
            });
    }
    else {
        console.log(fieldsResponse.status);
        return [];
    }
}