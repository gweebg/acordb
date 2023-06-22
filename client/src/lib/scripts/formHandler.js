import {inputs} from "$lib/stores/form.js";


export const addInput = () => {
    inputs.update(arr => {
        const id = arr.length; // Assign a unique ID to each input
        return [...arr, { id, value: { selectable: '', input: '' } }];
    });
}

export const updateSelectable = (id, selectable) => {

    inputs.update(arr => {
        return arr.map(item => {
            if (item.id === id) {
                return { ...item, value: { ...item.value, selectable: selectable.value} };
            }
            return item;
        });
    });
};


export const updateInput = (id, input) => {
    inputs.update(arr => {
        return arr.map(item => {
            if (item.id === id) {
                return { ...item, value: { ...item.value, input } };
            }
            return item;
        });
    });
}


export const removeInput = (id) => {
    inputs.update(arr => {
        return arr.filter(input => input.id !== id);
    });
}