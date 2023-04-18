import { z } from "zod";
import { superValidate } from 'sveltekit-superforms/server';
import {fail} from "@sveltejs/kit";

const loginSchema = z.object({

    email: z.string().email({message: "Invalid email address"}),
    password: z.string().min(1),
    remember: z.boolean()

});

export const load = async (event) => {

    const form = await superValidate(event, loginSchema);
    return { form };
};

export const actions = {

    default: async (event) => {

        const form = await superValidate(event, loginSchema);
        // console.log(form);

        if (!form.valid) {
            fail(400, { form });
        }

        return { form };

    }

};