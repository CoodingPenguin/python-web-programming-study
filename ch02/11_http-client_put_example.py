from http.client import HTTPConnection
from urllib.parse import urlencode

host = '127.0.0.1:8000'
# 파라미터에 대해 URL 인코딩
params = urlencode({
    'language': 'python',
    'name': '김석훈',
    'email': 'shkim@naver.com'
})
# 헤더 정의
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain'
}

# 연결 객체 생성
conn = HTTPConnection(host)
# 요청 보냄
conn.request('PUT', '', params, headers)
# 응답 객체 생성
resp = conn.getresponse()
print(resp.status, resp.reason)
# 응답 메시지 읽음
data = resp.read(300)
print(data.decode('utf-8'))
# 연결 닫음
conn.close()
