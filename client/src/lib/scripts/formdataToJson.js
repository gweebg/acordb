export const convert = (data) => {

    let result = {"Descritores": []};

    const asJsonString = JSON.stringify(Object.fromEntries(data));
    const asJson = JSON.parse(asJsonString);

    for (const key in asJson) {

        if (key.endsWith("[value]")) {
            let id = key.slice(7, 8);
            let actualKey = asJson[key];

            let value = asJson[`fields[${id}][value][input]`];

            result[actualKey] = value;
        }

        if (key.endsWith("[summary]")) {
            result["Sumário"] = asJson[key];
        }

        if (key.endsWith("[text]")) {
            result["Texto Integral"] = asJson[key];
        }

        if (key.endsWith("[decision]")) {
            result["Decisão"] = asJson[key];
        }

        if (key === "process") {
            result["Processo"] = asJson[key];
        }

        if (key === "url") {
            result["url"] = asJson[key];
        }

        if (key.startsWith("tags")) {
            result["Descritores"].push(asJson[key]);
        }

    }

    return result;
}