import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    Info = bsObj.find("div", {"class":"rPF6Lc", "jsname":"OYCkv"})
    #<h1 class="KY7mAb">QUALCOMM, Inc.</h1>
    #<div class="YMlKec fxKbKc">$144.94</div>
    name = Info.find("h1",{"class":"KY7mAb"}).text
    price = Info.find("div",{"class":"YMlKec fxKbKc"}).text
    # print(name,price)
    return {"name":name, "price":price}

def getCompanyInfo(code):
    url = "https://www.google.com/finance/quote/{}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    print(companyInfo)

url = ["QCOM:NASDAQ","066570:KRX"]

for s in url:
    getCompanyInfo(s)

# url = ["https://www.google.com/finance/quote/QCOM:NASDAQ",
#        "https://www.google.com/finance/quote/066570:KRX"]

