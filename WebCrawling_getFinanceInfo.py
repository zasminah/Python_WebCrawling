
#crawl() : Get Data
#parse() : Get specific information from Data

import requests #crawl
from bs4 import BeautifulSoup as bs #parse ,tag,class

def crawl(url):
    data = requests.get(url)
    print(data) #Responce such as 200(Success)
    return data.content

def parse(pageString):
    bsObj = bs(pageString, "html.parser")
    #< h1 class ="KY7mAb" > LG전자 < / h1 >
    #<div class="YMlKec fxKbKc">₩168,000.00</div>
    val = {"name":bsObj.find("h1", {"class": "KY7mAb"}).text}
    val.update({"price":bsObj.find("div",{"class":"YMlKec fxKbKc"}).text})
    print(val)
    return val

url = "https://www.google.com/finance/quote/066570:KRX"
pageString = crawl(url)# get PageSource Information
data = parse(pageString)
#print("Name : {name}, Price : {price}".format(name=data['name'],price=data['price']))
print("Name:",data.get('name'),"Price:",data.get('price'))
#print("Name:",data['name'],"Price:",data['price'])

