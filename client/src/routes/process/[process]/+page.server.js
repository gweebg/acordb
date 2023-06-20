import { PUBLIC_API_URL } from '$env/static/public';
export async function load({ fetch, params, locals }) {

    const process = await fetch(`${PUBLIC_API_URL}/records/${params.process}/`);
    const item2 = await process.json();
    let user;

    if (locals.user) user = locals.user;
    else user = null;

    return {
        "record": item2[0],
        "process": item2,
        user: user
    };
}