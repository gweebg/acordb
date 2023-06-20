import { fail, redirect } from "@sveltejs/kit";
import { PUBLIC_API_URL } from '$env/static/public';


const fetchIncomingRequests = async (authCookie) => {

    /* TODO */

}

const fetchOutgoingRequests = async (authCookie) => {

    /* TODO */

}

export const load = async ({cookies, locals}) => {

    if (!locals.user) {
        throw redirect(303, '/login');
    }

    const authCookie = cookies.get('AuthorizationToken');

    let requestData;
    if (authCookie) {

        if (locals.user.is_administrator) requestData = await fetchIncomingRequests();
        else requestData = await fetchOutgoingRequests();
    }

    return {
        user: locals.user,
        data: requestData
    };

};

