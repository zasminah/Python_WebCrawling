
import requests
from bs4 import BeautifulSoup as bs

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getProductInfo(li):
    info = li.find("div", {"class": "basicList_title__3P9Q7"})
    title = info.find("a")['title']
    price = li.find("span", {"class": "price_num__2WUXn"}).text
    price = price.replace("원","").replace(",","").replace(",","") # 100,000,000
    link = info.find("a")['href']
    return {"title": title, "price": price, "link": link}

def parse(pageString):
    bsObj = bs(pageString,"html.parser")
    # print(bsObj)
    ul = bsObj.find("ul",{"class":"list_basis"})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})

    productInfo = []

    for li in lis:
        try :
            productInfo.append(getProductInfo(li))
        except Exception as e :
            print("--error---", e)

    return productInfo

def getPageResult(pageNo,keyword):
    # url = "https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&cat_id=&frm=NVSHATC"
    url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%85%94%EC%B8%A0&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list".format(pageNo,keyword)
    pageString = crawl(url)
    products = parse(pageString)
    return products


pageResultTotal = []
for pageNo in range(1,8):
    pageResultTotal = pageResultTotal+getPageResult(pageNo,"셔츠")
# print(len(pageResultTotal))

# Save to file
import json
file = open("./셔츠.json","w+")
file.write(json.dumps(pageResultTotal))