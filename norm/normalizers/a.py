import os
import json
import re
from collections import OrderedDict
from utils import normDesc

def readInputData(file,):
    fullPath=os.path.join("acordãos_out/",file.split('/')[-1].split('.')[0]+".json")
    with open(fullPath, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data
#maior tag
#for data in map(readInputData,["atco1_acordaos","jcon_acordaos","jdgpj_acordaos","jsta_acordaos","jstj_acordaos","jtca_acordaos","jtcampca_acordaos","jtcampct_acordaos","jtcn_acordaos","jtrc_acordaos","jtre_acordaos","jtrg_acordaos","jtrl_acordaos","jtrp_acordaos"]):
#    ma=0
#    tagr=""
#    for item in data:
#        m=0
#        if "Descritores" in item:
#            for tag in item["Descritores"]:
#                m=max(m,len(tag))
#                if m==len(tag):
#                    t=tag
#        ma=max(ma,m)
#        if ma==m:
#            tagr=t
#    print(ma,tagr)
ma=set()
for data in map(readInputData,["atco1_acordaos","jcon_acordaos","jdgpj_acordaos","jsta_acordaos","jstj_acordaos","jtca_acordaos","jtcampca_acordaos","jtcampct_acordaos","jtcn_acordaos","jtrc_acordaos","jtre_acordaos","jtrg_acordaos","jtrl_acordaos","jtrp_acordaos"]):
    for item in data:
        if "Descritores" in item:
            ma.update(item["Descritores"])
print(len(ma))