import {PUBLIC_API_URL} from "$env/static/public";
import { error, fail } from "@sveltejs/kit";

export const fetchRuling = async (rulingId) => {

    let response;
    try {

        response = await fetch(`${PUBLIC_API_URL}/acordaos/${rulingId}/`);

    } catch (err) { throw error(500, "Server is down."); }

    if (response.ok) return response.json();
    else throw fail(404, "Ruling does not exist.");

}