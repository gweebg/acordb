from utils import readInputDataOrdered,normDesc,writeOutputData,emptyValue,handleProcesso,recorrido,legislação,areaTematica,jurisprudências,referencias,tribunalRecorrido
import re
data=readInputDataOrdered("/jtrl_acordaos.py")
maxReadFile=1E9



def apendice(item,k):
    if k not in ["Processo","Relator","Descritores","Nº do Documento","Data do Acordão","Votação","Texto Parcial","Meio Processual","Decisão","Sumário","url","tribunal","Texto Integral"]:
        if k in item["Processo"] or ("Texto Integral" in item.keys() and k in item["Texto Integral"]) or ("Sumário" in item.keys() and k in item["Sumário"]):
            if 'Apêndice' not in item.keys():
                item['Apêndice']=""
            item['Apêndice']+= f"{k} : {item[k]}\n"
            del item[k]
            
def handleTextoIntegral(item,k):
    if k=='Texto Integral':
        del item[k]
    elif k=="Decisão Texto Integral":
        item["Texto Integral"]=item[k]
        del item[k] 
        
def textoParcial(item,k):
    if k=="Texto Parcial":
        del item[k]


for item in data:    
    #apendice material
    collect_pairs=False
    for key,value in list(item.items()):
        if key == "Sumário":
            collect_pairs = True
        elif key == "Decisão Texto Integral":
            collect_pairs = False
        elif collect_pairs:
            if 'Apêndice' not in item.keys():
                item['Apêndice']=""
            item['Apêndice']+=f"{key}:{value}\n"
            del item[key] 
    for key in list(item.keys()):
        emptyValue(item,key)
    for key in list(item.keys()):
        handleTextoIntegral(item,key)
        textoParcial(item,key)
        legislação(item,key)
        jurisprudências(item,key)
        referencias(item,key)
        tribunalRecorrido(item,key)
        
    for key in list(item.keys()):
        apendice(item,key)

        
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]
    if "tribunal" not in list(item.keys()):
        item["tribunal"]="jtrl"
    normDesc(item)


    
    
writeOutputData("/jtrl_acordaos.py",data)
        
