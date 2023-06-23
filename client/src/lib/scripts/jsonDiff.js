import {diffWords} from 'diff';


export const compareRulings = (original, incoming) => {

    const asString = (jsonObj) => {

        let result = "";

        for (const key in jsonObj) {
            result += `<strong>${key}:</strong>\n\t${jsonObj[key]}\n\n`;
        }

        return result;
    }

    const differences = diffWords(asString(original), asString(incoming));

    let result = '<pre style="white-space: pre-wrap;">';
    differences.forEach(part => {
        const prefix = part.added ? '<span style="background-color: #2dbcab;">' : part.removed ? '<span style="background-color: #faab57;">' : '';
        const suffix = part.added || part.removed ? '</span>' : '';

        result += `${prefix}${part.value}${suffix}`;
    });
    result += '</pre>';

    return result;

}