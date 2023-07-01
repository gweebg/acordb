import { PUBLIC_API_URL } from '$env/static/public';
import { redirect } from "@sveltejs/kit";
import jwt_decode from "jwt-decode";

export const POST = async (requestEvent) => {

    const { request } = requestEvent;

    let body = await request.formData();
    let result = {};

    body.forEach((value, key) => result[key] = value);

    const credential = result.credential;
    // console.log(result)
    // console.log(credential)
    var decoded = jwt_decode(credential);
    let existingAccsReq = await fetch(`${PUBLIC_API_URL}/accounts/search/${decoded.email}/`);
    let existingAccs = await existingAccsReq.json();
    let b = null;

    if (existingAccs.length > 0) {
        b = JSON.stringify({ token: credential});
    } else {
        b = JSON.stringify({ token: credential, filiation: "DI" }); // TODO ! MUDAR ISTO PARA O REDIRECT DO REGISTO
    }

    // let token = await fetch(`${PUBLIC_API_URL}/accounts/login/google/`, {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: b,
    // })
    //     .then((res) => res.json())
    //     .then((data) => {
    //
    //         return data.access;
    //
    //     })
    //     .catch((err) => {
    //         console.error(err);
    //         return "";
    //     });

    let response = await fetch(`${PUBLIC_API_URL}/accounts/login/google/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: b
    })

    let token = "";
    if (response.ok) {

        token = await response.json();
        token = token.access;

    } else console.log(response.status);

    let redirectUrl = `http://localhost:5173/search?jwt=${token}`;

    // Create the redirect response
    const redirectResponse = new Response(null, {
        status: 302,
        headers: {
            location: redirectUrl,
        },
    });

    return redirectResponse;
}