import { redirect } from "@sveltejs/kit";
import {convert} from "$lib/scripts/formdataToJson.js";
import {PUBLIC_API_URL} from "$env/static/public";

export const load = async ({ locals }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user) {
        throw redirect(303, '/login');
    }

    // If user is authenticated we redirect him to his profile page.
    throw redirect(303, `/user/${locals.user.id}/profile`);

};

// export const actions = {
//
//     setAdmin: async ({ cookies, request }) => {
//
//         console.log("Action!");
//
//         const authCookie = cookies.get('AuthorizationToken');
//
//         if (authCookie) {
//
//             const data = await request.formData();
//             const userId = data.get('id');
//
//             let response;
//             try {
//
//                 response = await fetch(
//                     `${PUBLIC_API_URL}/accounts/user/${userId}/makeadmin`,
//                     {
//                         method: 'POST',
//                         headers: { 'Content-Type': 'application/json', 'Authorization': authCookie },
//                     }
//                 );
//
//             } catch (err) {
//                 return {
//                     success: false,
//                     message: "There is a problem on our side, please try again later."
//                 }
//             }
//
//             if (!response.ok) {
//                 return {
//                     success: false,
//                     message: "User not found."
//                 }
//             }
//
//         }
//
//     }
// };