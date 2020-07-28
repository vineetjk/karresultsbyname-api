
import json



with open('docs/data1.json','r') as inputFile:
    data = json.load(inputFile)
    d=[*data.values()]
    





with open('../data/data2.js','w') as outputfile:
    json.dump(d,outputfile,indent=4)