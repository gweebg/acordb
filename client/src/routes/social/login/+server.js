import { PUBLIC_API_URL } from '$env/static/public';
export const POST = async (requestEvent) => {
    const { request } = requestEvent;
    let body = await request.formData();
    let result = {};
    body.forEach((value, key) => result[key] = value);
    const credential = result.credential;
    console.log(result)
    console.log(credential)
    fetch(`${PUBLIC_API_URL}/accounts/login/google/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': result.g_csrf_token,
        },
        body: JSON.stringify({ token: credential }),
        credentials: 'include'
    })
        // .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            // if (data.error) {
            //     console.error(data.error);
            // } else {
            //     window.location.href = '/home';
            // }
        })
        .catch((err) => {
            console.error(err);
        });
    return new Response(credential)
}