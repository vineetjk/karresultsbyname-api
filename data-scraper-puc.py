import requests
import json
import unicodedata
from bs4 import BeautifulSoup as bs

data = dict()
raw_data_lst = list()


result = requests.post(
    "http://karresults.nic.in/resPUC_2020.asp", data={'reg': 100006})

soup = bs(result.content, 'html.parser')
tags = soup('td')


for t in tags:
    d = unicodedata.normalize("NFKD", str(t.string).strip())
    if len(d) != 0:
        raw_data_lst.append(d)
print(raw_data_lst)
if len(raw_data_lst)!=0:
    
    data[raw_data_lst[3]] = {
        raw_data_lst[0]:raw_data_lst[1],
        'reg_num':raw_data_lst[3],
        raw_data_lst[4]:raw_data_lst[6],
        raw_data_lst[7]:raw_data_lst[9],
        raw_data_lst[12]:raw_data_lst[15],
        raw_data_lst[16]:raw_data_lst[19],
        raw_data_lst[20]:raw_data_lst[22],
        raw_data_lst[23]:raw_data_lst[26],
        'CoreSubTotal':raw_data_lst[28],
        raw_data_lst[29]:raw_data_lst[30],
        'Percentage': str(round(float(raw_data_lst[30])*100/600,2))+'%',
        'CorePercentage':str(round(float(raw_data_lst[28])*100/400,2))+'%',
        raw_data_lst[31]:raw_data_lst[32]
    }
else : print("Invalid Entry")
print(data)

with open('docs/data.json','r+') as outputfile:
    try:
        new_data = json.load(outputfile)
        new_data.update(data)
        outputfile.seek(0)
        json.dump(new_data,outputfile)
    except:
        json.dump(data,outputfile)
