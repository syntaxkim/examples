from urllib.request import urlopen
from html.parser import HTMLParser

# Inherit from HTMLParser and override methods
class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet =set(x for x in parser.result)
    return dataSet

def main():
    url = "http://www.google.co.kr"

    with urlopen(url) as f:
        # Get page's encoding method and use it to decode data
        charset = f.info().get_param('charset')
        # data woulde be the body of HTTP response (HTML content)
        data = f.read().decode(charset)

    dataSet = parse_image(data)

    print("\n>>>> Fetch Images from", url)
    print('\n'.join(sorted(dataSet)))

if __name__ == '__main__':
    main()