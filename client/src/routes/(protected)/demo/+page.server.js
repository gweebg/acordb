import { redirect } from "@sveltejs/kit";

export const load = async ({ locals }) => {


    console.log("LOCALS:", locals);

    if (!locals.user) {
        console.log("Not authenticated!");
        throw redirect(303, '/login');
    }

};