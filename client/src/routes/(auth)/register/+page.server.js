import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import { fail } from "@sveltejs/kit";

const registerSchema = z.object({

    username: z.string().min(3),
    email: z.string().email(),
    password: z.string().min(1),
    tos: z.boolean()

});

export const load = async (event) => {

    const form = await superValidate(event, registerSchema);
    return { form };
};

export const actions = {

    default: async (event) => {

        const form = await superValidate(event, registerSchema);
        // console.log(form);

        /* Assert the TOS are checked. */
        if (form.data.tos === false) {
            form.errors["tos"] = ["You must accept the Terms of Service to create an account."];
        }

        if (!form.valid) {
            fail(400, { form });
        }

        return { form };

    }

};