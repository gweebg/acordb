import json 
import pandas as pd
with open("types_out.json") as json_file:
    data = {i.replace("_acordaos.json",""):k for i,k in json.load(json_file).items()}
keys=set()
for file,values in data.items():
    for k in values.keys():
        keys.add(k)
for key in keys:
    for value in data.values():
        if key not in value:
            value[key]=0


df = pd.DataFrame.from_dict(data, orient='columns')

df_sorted = df.sort_index()
df_sorted.to_excel('sheet.xlsx', index=True)


