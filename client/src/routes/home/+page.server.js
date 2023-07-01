import {fetchFields} from "$lib/scripts/utils.js";

export const load = async ({ locals }) => {

    const fields = await fetchFields();

    if (locals.user) {
        return {
            isAuthed: true,
            isAdmin: locals.user.is_administrator,
            fields: fields
        }
    }

    else {
        return {
            isAuthed: false,
            isAdmin: false,
            fields: fields
        }
    }

};