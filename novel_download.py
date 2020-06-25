#
#

import requests
from pyquery import PyQuery as pq

#  从小说目录页 http://www.jianlaixiaoshuo.com/ 获取所有页面链接
response = requests.get('http://www.jianlaixiaoshuo.com/')
response.encoding = response.apparent_encoding
doc = pq(response.text)

links = doc('dl > dd a')
for link in links.items():
    # print("http://www.jianlaixiaoshuo.com" + link.attr('href'))
    response = requests.get("http://www.jianlaixiaoshuo.com" + link.attr('href'))
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    title = doc('#BookCon > h1').text()
    content = doc('#BookText').text()

    # 使用上下文管理器打开文件
    with open('剑来.txt', mode='a+', encoding='utf-8') as f:
        f.write(title)
        f.write(content)
        f.write('/n')




