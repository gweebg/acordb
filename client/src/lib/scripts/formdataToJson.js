export const convert = (data) => {

    let result = {"Descritores": []};

    const asJsonString = JSON.stringify(Object.fromEntries(data));
    const asJson = JSON.parse(asJsonString);

    for (const key in asJson) {

        // Fields array handling.
        if (key.endsWith("[value][field]")) {
            let id = key.slice(7, 8);
            let actualKey = asJson[key];
            result[actualKey] = asJson[`fields[${id}][value][value]`];
        }

        // Body handling.
        if (key.endsWith("[summary]")) {
            result["Sumário"] = asJson[key];
        }

        if (key.endsWith("[text]")) {
            result["Texto Integral"] = asJson[key];
        }

        if (key.endsWith("[decision]")) {
            result["Decisão"] = asJson[key];
        }

        // Others
        if (key === "process") {
            result["Processo"] = asJson[key];
        }

        if (key === "url") {
            result["url"] = asJson[key];
        }

        // Tags
        if (key.startsWith("tags")) {
            result["Descritores"].push(asJson[key]);
        }

    }

    return result;
}