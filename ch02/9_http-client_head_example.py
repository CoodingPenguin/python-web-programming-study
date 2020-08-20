from http.client import HTTPConnection

# 연결 객체 생성
conn = HTTPConnection('www.example.com')

# 요청을 보냄
conn.request('HEAD', '/')

# 응답 객체 생성
resp = conn.getresponse()
print(resp.status, resp.reason)

# 응답 데이터 읽음
data = resp.read()
print(len(data))
print(data == b'')
