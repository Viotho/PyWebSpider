from re import U
import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    responce = requests.get(url)
    print(responce.text)