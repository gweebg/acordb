import {fetchFields} from "$lib/scripts/utils.js";

export async function load({ locals }) {

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    let fields = await fetchFields();

    return {
        user: user,
        fields: fields
    };
}