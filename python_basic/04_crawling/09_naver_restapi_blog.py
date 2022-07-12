# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os,sys,urllib.request,json

client_id = "MZ9ZRbV3eDKdiw3JaKYv"
client_secret = "KFR7kg2yME"
keyword = input('검색할 단어 >>> ')
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?display=10&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(type(response_body.decode('utf-8')))
    result = json.loads(response_body)
    # print(type(result))
    # print(result)
    for item in result['items']:
        print(item['bloggerlink'])
        res = urllib.request.urlopen(item['bloggerlink']).read()
        print(res.decode('utf-8'))
else:
    print("Error Code:" + rescode)