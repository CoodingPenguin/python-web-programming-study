from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = 'http://127.0.0.1:8000'
data = {
    'name': '코딩하는펭귄',
    'email': 'coodingpenguin@gmail.com',
    'url': 'cooding-penguin.netlify.app'
}
encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data=postData)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(100).decode('utf-8'))
