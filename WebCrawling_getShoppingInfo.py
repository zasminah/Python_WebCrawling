
import requests
from bs4 import BeautifulSoup as bs

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = bs(pageString,"html.parser")
    # print(bsObj)
    info = bsObj.find("div",{"class":"basicList_title__3P9Q7"}) #first
    title = info.find("a")['title']
    price = bsObj.find("span", {"class":"price_num__2WUXn"}).text
    link = info.find("a")['href']
    productInfo = {"title":title,"price":price,"link":link}
    print(productInfo)
    return []

url = "https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&cat_id=&frm=NVSHATC"

pageString = crawl(url)
products = parse(pageString)
print(products)