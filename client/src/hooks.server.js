
export const handle = async ({ event, resolve }) => {

    const authCookie = event.cookies.get('AuthorizationToken');

    if (authCookie) {

		try {

			var userResponse = await fetch("http://127.0.0.1:8000/accounts/personal/", 
			{
				method: 'GET', 
				headers: { 'Content-Type': 'application/json', 'Authorization': authCookie }

			});

			if (userResponse.ok) {

				const responseData = await userResponse.json();
				
				const sessionUser = {
					id: responseData.id,
					email: responseData.email,
					first_name: responseData.first_name,
					last_name: responseData.last_name,
					filiation: responseData.filiation
				};

				// @ts-ignore
				event.locals.user = sessionUser;

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