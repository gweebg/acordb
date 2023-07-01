import { writable } from 'svelte/store';

export const searchForm = writable(
    {
        tags: [],
        from_date: "",
        to_date: "",
        fields: [
            {
                id: "1",
                value: {field: "Relator", value: ""}
            }
        ]
    }
)