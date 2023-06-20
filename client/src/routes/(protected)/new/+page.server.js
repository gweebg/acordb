import {error, redirect} from "@sveltejs/kit";

export const load = async ({ locals }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user) {
        throw redirect(303, '/login');
    }

    // If the user is authenticated but is a consumer, block the access.
    if (locals.user.is_administrator === false) {
        throw error(404, { message: "You don't have the privilege to access this endpoint." });
    }

    return {user: locals.user};

};