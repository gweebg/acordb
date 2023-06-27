from utils import readInputData,normDesc,writeOutputData,recorrido,emptyValue,handleProcesso,jurisprudências,referencias,areaTematica,legislação,tribunalRecorrido
import re
data=readInputData("/jcon_acordaos.py")


for item in data:
    for key in list(item.keys()):
        emptyValue(item,key)
    
    for key in list(item.keys()):   
        recorrido(item,key)
        jurisprudências(item,key)
        referencias(item,key)
        areaTematica(item,key)
        legislação(item,key)
        tribunalRecorrido(item,key)
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]
    normDesc(item)
writeOutputData("/jcon_acordaos.py",data)
        
