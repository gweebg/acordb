import { PUBLIC_API_URL } from '$env/static/public';
export const POST = async (requestEvent) => {
    const { request } = requestEvent;
    let body = await request.formData();
    let result = {};
    body.forEach((value, key) => result[key] = value);
    const credential = result.credential;
    console.log(result)
    console.log(credential)
    let b = JSON.stringify({ token: credential, filiation: "DI" });
    fetch(`${PUBLIC_API_URL}/accounts/login/google/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: b,
    })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            //TRABALHA GWEE(E)
        })
        .catch((err) => {
            console.error(err);
        });
    return new Response(credential)
}