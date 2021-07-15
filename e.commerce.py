from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json

def data_Ecomerce():
    ECOMMERCE_API='https://webscraper.io/test-sites'
    ECOMMERCE_URL=requests.get(ECOMMERCE_API)
    data=ECOMMERCE_URL.json
    soup=BeautifulSoup(ECOMMERCE_URL.text,"html.parser")
    name = soup.find_all("h2")
    number=0
    list=[]
    for i in name:
        number += 1
        url = i.find("a")["href"]
        name = i.find("a").get_text().strip()
        Ecomerce_dict={'position':number,'Ecomerce_name':name,'Ecomerce_url':"https://webscraper.io"+url}
        list.append(Ecomerce_dict)
        with open("ECOMMERCE.json",'w') as f:
            json.dump(list,f,indent = 4)
    return (list)
data_Ecomerce()