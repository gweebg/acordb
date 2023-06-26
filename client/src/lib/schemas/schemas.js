import {z} from "zod";

export const accountSchema = z.object({

    first_name: z.string().min(3),
    last_name: z.string().min(3),
    email: z.string().email(),
    filiation: z.string(),
    password: z.string().min(1),
    tos: z.boolean()

});

export const loginSchema = z.object({

    username: z.string().email({message: "Invalid email address."}),
    password: z.string({
        required_error: "Please fill in the password field.",
        invalid_type_error: "Password must be a string."
    }).min(1),
    remember: z.boolean()

});