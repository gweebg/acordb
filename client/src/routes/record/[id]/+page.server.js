export async function load({ fetch, params }) {
    console.log(params)
    const record = await fetch(`http://127.0.0.1:8000/records?id=${params.id}`);
    const item1 = await record.json();
    console.log(item1)
    const process = await fetch(`http://127.0.0.1:8000/records/${item1[0].data.Processo}`);
    const item2 = await process.json();
    console.log(item2)
    return {"record": item1[0], "process": item2};
}