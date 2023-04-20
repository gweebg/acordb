import { redirect } from "@sveltejs/kit"

export const POST = async ({ cookies }) => {
	cookies.delete("AuthorizationToken");
	throw redirect(303, "/login");
}