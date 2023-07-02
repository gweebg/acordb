import { writable } from 'svelte/store';

export const newForm = writable({
       process: "",
       tags: [],
       fields: [
          {
             id: "1",
             value: {field: "Relator", value: ""}
          }
       ],
       url: "",
       body: {

          summary: "",
          decision: "",
          text: ""

       }
    }
);