import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser


# 이미지 파싱 클래스
# HTMLParser를 상속
class ImageParser(HTMLParser):
    # 특정 태그(img) 찾는 함수
    # 기존의 handle_starttag를 오버라이드
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        # <img src>를 찾아 result에 추가
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


# 이미지 탐색 및 다운로드
def download_image(url, data):
    # 'download' 폴더가 없으면 생성
    if not os.path.exists('download'):
        os.mkdir('download')

    # 이미지 파서 인스턴스 생성
    parser = ImageParser()
    # 이미지 파싱
    parser.feed(data)
    # 파싱 결과 저장
    dataSet = set(x for x in parser.result)

    # 파싱 결과를 정렬하여 하나씩 처리
    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)                          # src url
        # host+src로 baseurl 생성
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join('download', basename)     # 다운로드 경로 설정

        print('downloading..', imageUrl)
        # src로부터 이미지 다운로드
        # target 경로에 저장
        urlretrieve(imageUrl, targetFile)


def main():
    host = 'www.google.co.kr'

    conn = HTTPConnection(host)
    conn.request('GET', '')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()

    print('\n>>> download images from', host)
    # 다운로드 src url 지정
    # url 요소 6개를 인수로 받아 완성된 url 반환
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)


if __name__ == "__main__":
    main()
