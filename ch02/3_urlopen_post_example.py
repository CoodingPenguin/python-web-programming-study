# django로 임시 서버 만들고 다시 테스트
from urllib.request import urlopen

data = 'language=python&framework=django'
f = urlopen('http://127.0.0.1:8000', bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))
