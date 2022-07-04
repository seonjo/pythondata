import requests
import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://movie.naver.com/movie/point/af/list.naver?&page={}'
reviewlist =[]
for i in range(1,11):
    print(url.format(i))
    res = requests.get(url.format(i)).text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    table = soup.find('table',class_='list_netizen')
    for i,r in enumerate(table.select('tbody tr')):
        # print(i)
        # print(r)
        for j,c in enumerate(r.find_all('td')):
            if j==0:
                recode = int(c.text.strip())
                print('글번호:',recode)
            elif j==1:
                recode1 = c.select_one('a').text.strip()
                print('영화제목:',recode1)
                recode2 = c.select_one('em').text
                print('영화평점:',recode2)
                recode3 = c.text
                recode3 = recode3.replace(recode1,'')
                recode3 = recode3.replace('신고','')
                recode3 = re.sub('별점 - 총 10점 중[0-9]{1,2}','',recode3).strip()
                print(recode3)
                try:
                    movie_dic={
                        '제목': recode1,
                        '평점': recode2,
                        '감상평':recode3
                    }
                    reviewlist.append(movie_dic)
                except:
                    pass
print(reviewlist)