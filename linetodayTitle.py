import requests as rq
from bs4 import BeautifulSoup
import re


url= 'https://today.line.me/TW/pc/main/100457'
page_req = rq.get(url)

soup = BeautifulSoup(page_req .text,'html.parser')

#print(soup.prettify())

#for ptitle in soup.find('p'):
#for ptitle in soup.find('p').text:
#for ptitle in soup.find_all("p",{_class="content"})
#for ptitle in soup.select('p'):

listTitle = list()
listHttp = list()

"""取得標題"""
for ptitle in soup.select('.content'):

   # print(ptitle.text)
    listTitle.append(ptitle.text)
    #print(type(ptitle))
    #print(ptitle)



#print(soup.select('.))
"""取得連結"""
for a in soup.find_all('a', class_="lnk _link_home "):
    #print("Found the URL:", a['href'])
    listHttp.append(a['href'])

"""取出第2篇文章的標題跟連結
#print(listTitle[1])
print(listHttp[1])
"""
print(len(listTitle))
print(len(listHttp))

for i in range(0,10):
    print('no',i+1, listTitle[i], listHttp[i])
    if i == 8 :
        print('i==8')
        continue
