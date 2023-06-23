import { redirect } from "@sveltejs/kit";
import { PUBLIC_API_URL } from '$env/static/public';


const fetchRequests = async (authCookie) => {

    /* TODO: Returns the requests based on the authority of the authentication cookie. */
    return PUBLIC_API_URL + authCookie;

}


export const load = async ({cookies, locals}) => {

    if (!locals.user) {
        throw redirect(303, '/login');
    }

    const authCookie = cookies.get('AuthorizationToken');

    let requestData = await fetchRequests(authCookie);

    return {
        user: locals.user,
        data: requestData
    };

};

