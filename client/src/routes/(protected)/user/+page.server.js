import { redirect } from "@sveltejs/kit";

export const load = async ({ locals }) => {


    console.log("LOCALS:", locals);

    if (!locals.user) {
        throw redirect(303, '/home');
    }

};