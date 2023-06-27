import os
import json
import re
from collections import OrderedDict
from fuzzywuzzy import fuzz

allTags=set()

def readInputData(file,):
    fullPath=os.path.join("acordãos_in/",file.split('/')[-1].split('.')[0]+".json")
    with open(fullPath, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data

def readInputDataOrdered(file):
    fullPath=os.path.join("acordãos_in/",file.split('/')[-1].split('.')[0]+".json")
    with open(fullPath, encoding="utf8") as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)
    return data

def writeOutputData(file,data):
    fullPath=os.path.join("acordãos_out/",file.split('/')[-1].split('.')[0]+".json")
    with open(fullPath, "w", encoding="utf8") as outfile:
        json.dump(data, outfile)
        
def emptyValue(item,k):
    if item[k]=="":
        del item[k]
        
def handleProcesso(item,k):
    if k=="Processo":
        item[k]=item[k].replace("/","-")

def recorrido(item,k):
    isr = re.match(r"Recorrido (\d+)",k)
    if isr:
        if 'Recorrido' not in item.keys():
            item['Recorrido']=""
        item['Recorrido']+= f"{isr.group(1)} : {item[k]}\n"
        del item[k]

def legislação(item,k):
    isl = re.match(r"Legislação (.*)",k)
    if isl:
        if 'Legislações' not in item.keys():
            item['Legislações']=""
        item['Legislações']+= f"{isl.group(1)} : {item[k]}\n"
        del item[k]
        
def areaTematica(item,k):
    isat = re.match(r"Área Temática \d+",k)
    if isat:
        if 'Área Temática' not in item.keys():
            item['Área Temática']=""
        item['Área Temática']+= f"{item[k]};"
        del item[k]

def jurisprudências(item,k):
    isj = re.match(r"(.*)\s?Jurisprudência\s?(.*)",k)
    if isj:
        if 'Jurisprudências' not in item.keys():
            item['Jurisprudências']=""
        item['Jurisprudências']+= f"{isj.group(1)+isj.group(2)} : {item[k]}\n"
        del item[k]

def referencias(item,k):
    isr = re.match(r"Referência(?:s\s|\s)(.*)",k)
    if isr:
        if 'Referências' not in item.keys():
            item['Referências']=""
        item['Referências']+= f"{isr.group(1)} : {item[k]}\n"
        del item[k]

def normas(item,k):
    isn = re.match(r"Normas (.*)",k)
    if isn:
        if 'Normas' not in item.keys():
            item['Normas']=""
        item['Normas']+= f"{isn.group(1)} : {item[k]}\n"
        del item[k]

def doDiarioDaRepublica(item,k):
    isdDR = re.match(r"(.+) do Diário da República",k)
    if isdDR:
        if 'Diário da República' not in item.keys():
            item['Diário da República']=""
        item['Diário da República']+= f"{isdDR.group(1)} : {item[k]}\n"
        del item[k]
        
def doBoletimdoMJ(item,k):
    isdBMJ = re.match(r"(.+) do Boletim do M.J",k)
    if isdBMJ:
        if 'Boletim do M.J' not in item.keys():
            item['Boletim do M.J']=""
        item['Boletim do M.J']+= f"{isdBMJ.group(1)} : {item[k]}\n"
        del item[k]

def tribunalRecorrido(item,k):
    ist = re.match(r"Tribunal(?:.*)",k)
    if ist:
        item["Tribunal Recurso"]=item[k]
        if 'Tribunal Recurso' != k:
            del item[k]
    else:
        ispnt = re.match(r"Processo no Tribunal(?:.*)",k)
        if ispnt:
            item["Processo no Tribunal Recurso"]=item[k]
            if 'Processo no Tribunal Recurso' != k:
                del item[k]
                
                
def calculate_similarity(word1, word2):
    similarity_score = fuzz.ratio(word1, word2) / 100
    return similarity_score


def replace_matching_words(tags):
    global allTags
    r=set()
    for tag_word in tags:
        if tag_word not in allTags:
            if tag_word+'.' in allTags:
                r.add(tag_word+'.')
            elif tag_word[-1]=='.' and tag_word[:-1] in allTags:
                r.add(tag_word[:-1])
            else:
                allTags.add(tag_word)
                r.add(tag_word)
        else:
            r.add(tag_word)
            
    return list(r)
import unicodedata

def remove_accents(input_string):
    nfkd_form = unicodedata.normalize('NFKD', input_string)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def normDesc(item):

    desc=item["Descritores"]
    res=set()
    for string in desc:
        elements = re.split(r"\n+|\t\t+|\s\s+|\;|\.\s",string)
        cleaned_elements = [elem.strip() for elem in elements]
        res.update(map(remove_accents,filter(lambda x:len(x)>1,cleaned_elements)))
    item["Descritores"]=replace_matching_words(res)
    
