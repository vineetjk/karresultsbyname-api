
import json



with open('docs/data.json','r+') as inputFile:
    data = json.load(inputFile)
    d=[*data.values()]
    export = "const results = " + str(d)


fh = open('../data/sample-data.js','w+')
fh.write(export)