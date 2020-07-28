import requests
import json
import re
import unicodedata
from bs4 import BeautifulSoup as bs
import time
start_time = time.time()
print("Application Started...   " + str(time.time()))
data = dict()
raw_data_lst = list()
u = 164539
print("Collecting Data Please wait...   " + str(time.time()))
while u <183300:
    print(u)
    data.clear()
    raw_data_lst.clear()
    result = requests.post(
        "http://karresults.nic.in/resPUC_2020.asp", data={'reg': u})


    soup = bs(result.content, 'html.parser')
    tags = soup('td')
    u=u+1


    for t in tags:
        d = unicodedata.normalize("NFKD", str(t.string).strip())
        # print(d)
        if len(d) != 0:
            if len(re.findall('^[0-9]{1,2}[:.,-]?$',d)) == 0:
                raw_data_lst.append(d)
    # print(raw_data_lst)


    lenData=len(raw_data_lst)
    if len(raw_data_lst)!=0:
        try:
            data[raw_data_lst[3]] = {
                raw_data_lst[0]:raw_data_lst[1], #name
                'reg_num':raw_data_lst[3], # reg num
                raw_data_lst[4]:raw_data_lst[5], #eng eque
                raw_data_lst[6]:raw_data_lst[7], #kan eque
            # raw_data_lst[8]:raw_data_lst[9], None value
            raw_data_lst[10]:raw_data_lst[11], #phy eque
            raw_data_lst[12]:raw_data_lst[13], #chem eque
            raw_data_lst[14]:raw_data_lst[15], #math eque 
            raw_data_lst[16]:raw_data_lst[17], #bio eque
            'part_b_total':raw_data_lst[19], #part b total
                raw_data_lst[20]:raw_data_lst[21], #grand total
                raw_data_lst[lenData-2]:raw_data_lst[lenData-1], #final grade


                'CoreSubTotal':raw_data_lst[19],
                
                'Percentage': str(round(float(raw_data_lst[21])*100/600,2))+'%',
                'CorePercentage':str(round(float(raw_data_lst[19])*100/400,2))+'%',
                
            }
        except:
            continue
    else : print("Invalid Entry")
    # print(data)



    with open('docs/data6.json','r+') as outputfile:
        try:
            new_data = json.load(outputfile)
            new_data.update(data)
            outputfile.seek(0)
            json.dump(new_data,outputfile,indent=4)
        except:
            json.dump(data,outputfile,indent=4)
    
print("Finished Collecting Data....   " + str(time.time()))
print("Time Elapse : "+str((time.time() - start_time)) +" seconds" )
