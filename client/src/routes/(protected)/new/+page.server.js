import {error, fail, redirect} from "@sveltejs/kit";
import {PUBLIC_API_URL} from "$env/static/public";
import {convert} from "$lib/scripts/formdataToJson.js";

import {fetchFields} from "$lib/scripts/utils.js";

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

    new: async ({ cookies, request }) => {

        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            let data = await request.formData(); /* This holds the form data, un-formatted because of black magic. */
            let final = convert(data); /* This holds the form data, formatted as readable JSON. */

            if (!final.Processo || final.Descritores.length === 0) {
                return fail(400, "Os campos 'Processo' e 'Descritores' são obrigatórios.");
            }

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_API_URL}/acordaos/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(final)
                    }
                );

            } catch (err) {
                return fail(400, "Houve um problema do nosso lado, tente mais tarde.");
            }

            if (!response.ok) {
                return fail(400, "Algo de mal aconteceu com o seu pedido, tente novamente.")
            }


            let content = await response.json();
            return content.acordao;
        }
    },

    upload: async ({ cookies, request }) => {

        const authCookie = cookies.get('AuthorizationToken');

        if (authCookie) {

            let data = await request.formData(); /* This holds the form data, un-formatted because of black magic. */
            console.log(data);

            const asJsonString = JSON.stringify(Object.fromEntries(data));
            const asJson = JSON.parse(asJsonString);
            const asObj = {};

            for (const key in asJson) {

                if (key.startsWith("Descritores")) {

                    if (!asObj["Descritores"]) asObj["Descritores"] = [];
                    asObj["Descritores"].push(asJson[key])

                } else asObj[key] = asJson[key];

            }

            let response;
            try {

                response = await fetch(
                    `${PUBLIC_API_URL}/acordaos/`,
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                        body: JSON.stringify(asObj)
                    }
                );

            } catch (err) {
                return fail(400, "Houve um problema do nosso lado, tente mais tarde.");
            }

            if (!response.ok) {
                return fail(400, "Algo de mal aconteceu com o seu pedido, tente novamente.")
            }


            let content = await response.json();
            return content.acordao;
        }
    }
};