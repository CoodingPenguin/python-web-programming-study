from urllib.request import urlopen
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


# 이미지를 찾는 함수
def parse_image(data):
    parser = ImageParser()  # ImageParser 인스턴스 생성
    parser.feed(data)       # HTML 문장 파싱
    dataSet = set(x for x in parser.result)     # 파싱 결과
    return dataSet

# 메인 함수


def main():
    url = 'http://www.google.co.kr'

    # 구글 첫 페이지로 접속
    with urlopen(url) as f:
        charset = f.info().get_param('charset')  # 구글 페이지 인코딩 방식
        data = f.read().decode(charset)         # 으로 디코딩

    dataSet = parse_image(data)  # HTML에서 이미지 파싱

    print('\n>> Fetch images from', url)
    print('\n'.join(sorted(dataSet)))


if __name__ == '__main__':
    main()
