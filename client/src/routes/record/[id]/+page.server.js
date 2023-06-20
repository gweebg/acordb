import { PUBLIC_API_URL } from '$env/static/public';
export async function load({ fetch, params }) {
    // console.log(params)
    // console.log(`${PUBLIC_API_URL}/records?id=${params.id}`);
    const record = await fetch(`${PUBLIC_API_URL}/records?id=${params.id}`);
    const item1 = await record.json();
    // console.log(item1)
    const process = await fetch(`${PUBLIC_API_URL}/records/${item1[0].data.Processo}`);
    const item2 = await process.json();
    // console.log(item2)
    return {"record": item1[0], "process": item2};
}