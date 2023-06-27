from utils import readInputData,writeOutputData,emptyValue,doDiarioDaRepublica,doBoletimdoMJ,areaTematica,normas,legislação,jurisprudências,referencias,normDesc
import re
data=readInputData("/atco1_acordaos.py")



for item in data:
    for key in list(item.keys()):
        emptyValue(item,key)
    for key in list(item.keys()):   
        doDiarioDaRepublica(item,key)
        doBoletimdoMJ(item,key)
        areaTematica(item,key)
        normas(item,key)
        legislação(item,key)
        jurisprudências(item,key)
        referencias(item,key)
    normDesc(item)  
writeOutputData("/atco1_acordaos.py",data)
        