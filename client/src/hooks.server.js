import { PUBLIC_API_URL } from '$env/static/public';

import { SvelteKitAuth } from "@auth/sveltekit"
import Google from '@auth/core/providers/google';
import Credentials from "@auth/core/providers/credentials"

// export const handle = SvelteKitAuth({
//   providers: [
// 	Credentials({
// 		async authorize(credentials) {
// 		  const authResponse = await fetch("/users/login", {
// 			method: "POST",
// 			headers: {
// 			  "Content-Type": "application/json",
// 			},
// 			body: JSON.stringify(credentials),
// 		  })
  
// 		  if (!authResponse.ok) {
// 			return null
// 		  }
  
// 		  const user = await authResponse.json()
  
// 		  return user
// 		},
// 	  }),
//     Google({
		// clientId: "316555827922-thlb7qjblpqovk9033h29ub4rejimaqd.apps.googleusercontent.com",
    	// clientSecret: "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"
// 	})
//   ]
// });

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

				// This is dumb, at this point just = responseData.
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