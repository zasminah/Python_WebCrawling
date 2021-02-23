import pandas as pd
pd.set_option('display.max_colwidth', -1) # -1 : 전체출력
import openpyxl

def save(df,filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Sheet1')
    writer.save()
def printBrandCount(brand):
    print(brand)
    dfFiltered = df[df['title'].str.contains(brand)]
    print(dfFiltered.count())
    # print(dfFiltered['price'])
def printPriceRange(price1, price2):
    dfFiltered = df[(df['price'] > price1) & (df['price'] <= price2)]
    dfSorted = dfFiltered.sort_values(['price'], ascending=[0])
    # print(dfSorted.head(10)['price'])
    # print(dfSorted.tail(10)['price'])
    print(dfSorted)

#dataframe => 표
df = pd.read_json("./셔츠.json")

# print(df.count())

# [1] Save to Excel
save(df,"./셔츠.xlsx")

# [2] filter 10 items, head <-> tail
# print(df.head(10))

# [3] filter Brand Name
# brands = ["헤지스", "닥스"]
# for brand in brands:
#     printBrandCount(brand)

# [4] filter Price
# dfFiltered = df[(df['price'] >= '10000') & (df['price'] <= '50000')]
# dfFiltered = df[(df['price'].str.replace('원','') > '50000']
# test = df['price'].str.replace('원','') > '50000'
# print(test)
# print(dfFiltered)
# print(dfFiltered.count())
#
# # [5] filter Price
# dfSorted = df.sort_values(['price'], ascending=[0])
# print(dfSorted)

# printPriceRange(90000,150000)
