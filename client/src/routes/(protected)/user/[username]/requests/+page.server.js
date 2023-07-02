import {error, fail, redirect} from "@sveltejs/kit";
import { PUBLIC_SERVER_API_URL } from '$env/static/public';
import {superValidate} from "sveltekit-superforms/server";


const fetchRequests = async (authCookie) => {

    /* TODO: Returns the requests based on the authority of the authentication cookie. */

    let requests = [];

    try {

        const response = await fetch(`${PUBLIC_SERVER_API_URL}/accounts/requests/`,
    {
            method: 'GET',
            headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
        });

        if (response.ok) {
            requests = await response.json();
        }
        else {
            console.log(`[Error ${response.status}] fetchRequests @ resquests`);
        }

    } catch (err) {

        console.log(`[Error] fetchRequests @ resquests ${err}`);

    }

    return requests;

}


export const load = async ({cookies, locals}) => {

    if (!locals.user) {
        throw redirect(303, '/login');
    }

    const authCookie = cookies.get('AuthorizationToken');
    let requestData;

    if (authCookie) requestData = await fetchRequests(authCookie);
    else throw redirect(301, '/login');

    return {
        user: locals.user,
        data: requestData
    };

};


export const actions = {

    accept: async ({ cookies, request, locals }) => {

        const authCookie = cookies.get('AuthorizationToken');
        if (authCookie) {

            const data = await request.formData();

            try {

                const response = await fetch(`${PUBLIC_SERVER_API_URL}/acordaos/changeRequest/${data.get('id')}/`,
            {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                    body: JSON.stringify({
                        status:"accepted",
                        reviewer: locals.user.email
                    })
                });

                if (!response.ok) {
                    console.log(`[Error ${response.status}] actions:accept @ requests (page.server.js)`);
                }


            } catch (err) {console.log(`[Error] actions:accept @ requests (page.server.js) ${err}`);}

        }
    },

    deny: async ({ cookies, request }) => {

        const authCookie = cookies.get('AuthorizationToken');
        if (authCookie) {

            const data = await request.formData();

            try {

                const response = await fetch(`${PUBLIC_SERVER_API_URL}/acordaos/changeRequest/${data.get('id')}/`,
                    {
                        method: 'DELETE',
                        headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
                    });

                if (!response.ok) {
                    console.log(`[Error ${response.status}] actions:deny @ requests (page.server.js)`);
                }


            } catch (err) {console.log(`[Error] actions:deny @ requests (page.server.js) ${err}`);}

        }
    },
};

