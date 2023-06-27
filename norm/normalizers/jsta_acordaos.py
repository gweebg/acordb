from utils import readInputData,normDesc,writeOutputData,emptyValue,handleProcesso,recorrido,legislação,areaTematica,jurisprudências,referencias,tribunalRecorrido
import re
data=readInputData("/jsta_acordaos.py")
        
        
def apendice(item,k):
    if k not in ["Área Temáticas","Jurisprudências","Referências",'Texto Integral','Recorrido','Legislações','Área Temáticas',"Processo","Data do Acordão","Tribunal","Relator","Descritores","Nº Convencional","Nº do Documento","Data de Entrada","Recorrente","Votação","CRITÉRIO","url","tribunal"]:
        if "Texto Integral" in item.keys():
            if k in item["Texto Integral"]:
                if 'Apêndice' not in item.keys():
                    item['Apêndice']=""
                item['Apêndice']+= f"{k} : {item[k]}\n"
                del item[k]

for item in data:
    for key in list(item.keys()):
        emptyValue(item,key)
        
    for key in list(item.keys()):
        recorrido(item,key)
        legislação(item,key)
        areaTematica(item,key)
        jurisprudências(item,key)
        referencias(item,key)
        tribunalRecorrido(item,key)
    for key in list(item.keys()):
        apendice(item,key)
        
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]    
    normDesc(item)
    
writeOutputData("/jsta_acordaos.py",data)
        
