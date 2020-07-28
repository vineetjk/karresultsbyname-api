import json
fname = 'docs/data2.json'


with open('docs/data2.json','r+') as outputfile:
        try:
            new_data = json.load(outputfile)
            
print(data)
