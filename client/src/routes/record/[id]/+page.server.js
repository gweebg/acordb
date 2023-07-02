import {fetchRecord} from "$lib/scripts/fetchRuling.js";

export async function load({ params, locals }) {

    const record = await fetchRecord(params.id);

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    return {
        ruling: record,
        user: user,
    };
}

