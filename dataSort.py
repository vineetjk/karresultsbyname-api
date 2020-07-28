import json
fname = 'docs/data2.json'
fh = open(fname)
print(fh)

data = json.load(fh)
values = data.keys()
print(data)
