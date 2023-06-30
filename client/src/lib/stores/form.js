import { writable } from 'svelte/store';

export const inputs = writable([{ id: 0, value: { selectable: '', input: '' } }]);

export const process = writable("");

export const url = writable("");

export const tags = writable([]);

export const body = writable({
   summary: "",
   decision: "",
   text: ""
});