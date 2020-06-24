#

import requests

response = requests.get('http://www.jianlaixiaoshuo.com/book/1.html')
response.encoding = response.apparent_encoding

print(response.text)

