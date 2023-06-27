from utils import readInputData,normDesc,writeOutputData,emptyValue,handleProcesso,tribunalRecorrido
import re
data=readInputData("/jdgpj_acordaos.py")

def isRecurso(item,k): # visto que so indica Se Relator,Data do Acórdão e Decisão existem
    if k=="Recursos":
        del item[k]

def standardizeAcordão(item,key):
    if key=='Data do Acórdão':
        item['Data do Acordão']=item[key]
        del item[key]


for item in data:
    for key in list(item.keys()):
        emptyValue(item,key)
        standardizeAcordão(item,key)
        
    for key in list(item.keys()): 
        isRecurso(item,key)
        tribunalRecorrido(item,key)
    if "Descritores" not in list(item.keys()):
        item["Descritores"]=[]
    normDesc(item)
    
    
writeOutputData("/jdgpj_acordaos.py",data)
        
