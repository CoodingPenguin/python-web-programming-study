from urllib.request import Request, HTTPCookieProcessor, build_opener

url = 'http://127.0.0.1:8000/cookie/'

# first GET request with cookie handler

# 쿠키 핸들러 생성
# 쿠키 데이터 지정은 디폴트로 CookieJar 객체 사용
cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)

req = Request(url)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))

print('-'*30)

# second POST request
data = 'language=python&framework=django'
encData = bytes(data, encoding='utf-8')

req = Request(url, encData)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))
