import requests
import bs4
import re

url = "https://sci-hub.tw/10.1080/01431160310001619607"

r = requests.get(url)

#HTTP请求的返回状态，比如，200表示成功，404表示失败
# print (r.status_code)
# #HTTP请求中的headers
# print (r.headers)
# #从header中猜测的响应的内容编码方式
# print (r.encoding)
# #从内容中分析的编码方式（慢）
# print (r.apparent_encoding)

# print(r.text)

html = r.text

soup = bs4.BeautifulSoup(html, 'lxml')

# print(soup.prettify())

# print(soup.a)

for x in soup.find_all('a',string = re.compile('save')):
    print(x)
    link = x.get('onclick')
    print(link)