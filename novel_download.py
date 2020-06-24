#

import requests
from pyquery import PyQuery as pq

response = requests.get('http://www.jianlaixiaoshuo.com/book/1.html')
response.encoding = response.apparent_encoding
# print(response.text)

doc = pq(response.text)

title = doc('#BookCon > h1').text()
content = doc('#BookText').text()

print(content)

