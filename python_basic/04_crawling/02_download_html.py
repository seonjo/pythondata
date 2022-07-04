# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%97%AC%EB%A6%84%EB%B0%94%EB%8B%A4

import urllib.request
import urllib.parse

url = 'https://search.naver.com/search.naver'
values = {
    'where':'nexearch',
    'sm':'top_hty',
    'fbm':'1',
    'ie':'utf8',
    'query':'여름바다'
}
param =urllib.parse.urlencode(values)
url = url + '?' + param
print(url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)