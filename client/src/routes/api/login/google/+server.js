import { PUBLIC_API_URL } from '$env/static/public';
import jwt_decode from "jwt-decode";
export const POST = async (requestEvent) => {
    const { request } = requestEvent;
    let body = await request.formData();
    let result = {};
    body.forEach((value, key) => result[key] = value);
    const credential = result.credential;
    console.log(result)
    console.log(credential)
    var decoded = jwt_decode(credential);
    let existingAccsReq = await fetch(`${PUBLIC_API_URL}/accounts/search/${decoded.email}/`);
    let existingAccs = await existingAccsReq.json();
    let b = null;
    if (existingAccs.length > 0) {
        b = JSON.stringify({ token: credential});
    } else {
        b = JSON.stringify({ token: credential, filiation: "DI" }); // ! MUDAR ISTO PARA O REDIRECT DO REGISTO  
    }
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