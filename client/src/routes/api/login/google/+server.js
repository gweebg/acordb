import { PUBLIC_API_URL } from '$env/static/public';
import { redirect } from "@sveltejs/kit";
import jwt_decode from "jwt-decode";
import { browser } from '$app/environment';

export const GET = () => {
    let redirectUrl = `http://localhost/home`;
    if (browser) { // to prevent error window is not defined, because it's SSR
        window.location.href = redirectUrl;
    }
    const redirectResponse = new Response(null, {
        status: 200,
        // headers: {
        //     location: redirectUrl,
        // },
    });
    return redirectResponse;
}

export const POST = async (requestEvent) => {

    const { request } = requestEvent;

    let body = await request.formData();
    let result = {};

    body.forEach((value, key) => result[key] = value);

    const credential = result.credential;
    // console.log(result)
    // console.log(credential)
    let b = JSON.stringify({ token: credential});

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

    let redirectUrl = `http://localhost/api/redirectLogin?jwt=${token}`;

    // Create the redirect response
    const redirectResponse = new Response(null, {
        status: 303,
        headers: {
            location: redirectUrl,
        },
    });

    return redirectResponse;
}