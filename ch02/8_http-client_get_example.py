from http.client import HTTPConnection

host = 'www.example.com'    # url이 아니라 host

# 1. 연결 객체 생성
conn = HTTPConnection(host)

# ==== 첫 번째 요청 ====
# 2. 요청을 보냄
conn.request('GET', '/')
# 3. 응답 객체 생성
r1 = conn.getresponse()
print(r1.status, r1.reason)
# 4. 응답 객체 읽음
data1 = r1.read()
# ======================

# 첫 번째 요청이 끝나야 두 번째 요청이 가능
# ==== 두 번째 요청 ====
conn.request('GET', '/')
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
print(data2.decode())
# ======================

# 5. 연결을 닫음
conn.close()
