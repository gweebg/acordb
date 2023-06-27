import { fetchRuling } from "$lib/scripts/fetchRuling.js";


export async function load({ params, locals }) {

    const ruling = await fetchRuling(params.ruling);

    let user;

    if (locals.user) user = locals.user;
    else user = null;

    return {
        ruling: ruling,
        user: user
    };
}