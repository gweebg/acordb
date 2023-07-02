import {newForm} from "$lib/stores/form.js";

export const addInput = () => {

    newForm.update(formData => {

        const id = formData.fields.length; // Assign a unique ID to each input

        return {
            ...formData,
            fields: [...formData.fields, {id, value: {field: "", value: ""}}]
        }

    });

}

export const removeInput = (id) => {
    newForm.update(formData => {

        return {
            ...formData,
            fields: formData.fields.filter(item => item.id !== id)
        }

    });
}