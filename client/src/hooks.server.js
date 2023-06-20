import { PUBLIC_API_URL } from '$env/static/public';
export const handle = async ({ event, resolve }) => {

    const authCookie = event.cookies.get('AuthorizationToken');

    if (authCookie) {

		try {

			var userResponse = await fetch(`${PUBLIC_API_URL}/accounts/user/`,
			{
				method: 'GET', 
				headers: { 'Content-Type': 'application/json', 'Authorization': authCookie }

			});

			if (userResponse.ok) {

				const responseData = await userResponse.json();

				event.locals.user = {
					id: responseData.id,
					email: responseData.email,
					first_name: responseData.first_name,
					last_name: responseData.last_name,
					filiation: responseData.filiation,
					is_administrator: responseData.is_administrator
				};

			}
			else {
				console.log(userResponse.status);
			}

		} catch (err) {

			/* The server is down, alert the user. */
			console.log("Server is down - ", err);
		}
	}

	return await resolve(event);
  
};