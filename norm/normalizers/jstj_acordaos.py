from utils import readInputData,normDesc,writeOutputData,emptyValue,handleProcesso,recorrido,legislação,areaTematica,jurisprudências,referencias,tribunalRecorrido
import re
data=readInputData("/jstj_acordaos.py")
maxReadFile=1E9



def apendice(item,k):
    if k not in ["Processo","Nº Convencional","Relator","Descritores","Data do Acordão","Votação","Texto Integral","Privacidade","Meio Processual","Decisão","Sumário","url","tribunal","Nº do Documento"]:
        if k in item["Processo"] or ("Texto Integral" in item.keys() and k in item["Texto Integral"]):
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

for item in data:    
    for key in list(item.keys()):
        emptyValue(item,key)
        
    for key in list(item.keys()):
        legislação(item,key)
        jurisprudências(item,key)
        referencias(item,key)
        tribunalRecorrido(item,key)
        
    for key in list(item.keys()):    
        handleTextoIntegral(item,key)
        
    for key in list(item.keys()):
        apendice(item,key)
        
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]
    normDesc(item)

    
    
writeOutputData("/jstj_acordaos.py",data)
        
