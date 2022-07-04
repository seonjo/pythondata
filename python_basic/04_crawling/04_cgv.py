import urllib.request
from bs4 import BeautifulSoup
import requests

url = 'http://www.cgv.co.kr/movies/'
# res = urllib.request.urlopen(url)
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
# print(soup.prettify())
result = soup.select('strong.title')
# print(result)
name = []
for item in result:
    name.append(item.text)
# print(name)

result = soup.select('span.thumb-image img')
# print(result)
img=[]
for item in result:
    # print(type(item))
    img.append(item['src'])
# print(img)
print(list(zip(name,img)))