import { PUBLIC_SERVER_API_URL } from "$env/static/public";


export const capitalize = (word) => {
    return word.replace(
        /\w\S*/g,
        function(txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
    );
}


export const fetchFields = async () => {

    const fieldsResponse = await fetch(
        `${PUBLIC_SERVER_API_URL}/acordaos/fields/`,
        {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }

        });

    if (fieldsResponse.ok) {

        /* This data is in the format [{name:"..."},{name:"..."},...] */
        const responseData = await fieldsResponse.json();

        /* Reserved fields that are already put out for the user to fill in. */
        const reservedFields = ['url', 'Processo', 'Descritores', 'Texto Integral', 'Sumário', 'Decisão']

        /* Return the flattened list with the reserved fields removed. */
        return responseData
            .map((value) => { return value.name})
            .filter((value) => {
                return !reservedFields.includes(value);
            });
    }
    else {
        console.log(fieldsResponse.status);
        return [];
    }
}

export const checkValue = (value) => { return value || "N/A" }

export const normalizeString = (string) => {return string.normalize("NFD").replace(/[\u0300-\u036f]/g, "")}