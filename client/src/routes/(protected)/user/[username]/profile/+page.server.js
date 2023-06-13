import { redirect } from "@sveltejs/kit";

export const load = async ({ locals, params }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user || params.username != locals.user.id) {
        throw redirect(303, '/login');
    }

    // TODO: Get user statistics and append to locals.
    locals.user.favorites = 30;
    locals.user.createdAt = "30 Jul 2021";
    locals.user.addedRecords = 312;

    // If user is authenticated we return its user data to the page.
    return {user: locals.user};

};