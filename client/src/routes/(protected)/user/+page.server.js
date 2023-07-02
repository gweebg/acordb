import { redirect } from "@sveltejs/kit";

export const load = async ({ locals }) => {

    // If user is not authenticated then we redirect him to login page.
    if (!locals.user) {
        throw redirect(303, '/login');
    }

    // If user is authenticated we redirect him to his profile page.
    throw redirect(303, `/user/${locals.user.id}/profile`);

};
