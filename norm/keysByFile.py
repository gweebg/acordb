import os
import json

files = os.listdir("acordãos_out/")
dic={}
total={}

def append(dic,k):
    if k in dic: dic[k]+=1
    else: dic[k]=1
def appendLen(dic,k,l):
    if k+'len' in dic: dic[k+'len']+=l
    else: dic[k+'len']=l

for file in files:
    file_path = os.path.join("acordãos_out/", file)
    print(file)
    total[file]=0
    dic[file]={}
    with open(file_path) as json_file:
        data = json.load(json_file)
        for item in data:
            total[file]+=1
            for item_key in item.keys():
                append(dic[file],item_key)
                appendLen(dic[file],item_key,len(item[item_key]))

for file in dic.keys():
    dic[file]['TOTAL']=total[file]
for file in dic.keys():
    for key in dic[file].keys():
        if key.endswith("len"):
            dic[file][key] = dic[file][key]/dic[file]['TOTAL']
    
    

with open("types_out.json", "w") as outfile:
    json.dump(dic, outfile)
