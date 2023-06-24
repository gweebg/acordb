export const load = async ({ locals }) => {

    if (locals.user) return {isAuthed: true, isAdmin: locals.user.is_administrator};
    else return {isAuthed: false};

};