import imp
from sympy import im


from urllib.parse import urlparse, urlencode, quote

if __name__ == '__main__':
    base_url = 'https://www.baidu.com'
    parsed = urlparse(base_url)
    print(parsed)


