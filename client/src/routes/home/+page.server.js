export const load = async ({ locals }) => {

    if (locals.user) return {isAuthed: true};
    else return {isAuthed: false};

};