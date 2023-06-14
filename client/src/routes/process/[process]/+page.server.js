export async function load({ fetch, params }) {
    const process = await fetch(`http://127.0.0.1:8000/records/${params.process}/`);
    const item2 = await process.json();
    console.log(item2)
    return {"record": item2[0], "process": item2};
}