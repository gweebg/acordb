import { PUBLIC_API_URL } from '$env/static/public';
export async function load({ fetch, params }) {
    const process = await fetch(`${PUBLIC_API_URL}/records/${params.process}/`);
    const item2 = await process.json();
    // console.log(item2)
    return {"record": item2[0], "process": item2};
}