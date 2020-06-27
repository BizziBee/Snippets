#
#

import requests
from pyquery import PyQuery as pq

def _init():
    # https://xs.sogou.com/list/9315264508
    global strMuluAddr
    strMuluAddr = ''

    # body > div.wrapper.mulu-wp > div.box-center.box-content.clear > div > ul > li > a
    global strLinkSelector
    strLinkSelector = ''

    # https://xs.sogou.com
    global strPrefixAddr
    strPrefixAddr = ''

    # body > div > div > h1
    global strTitleSelector
    strTitleSelector = ''

    # #contentWp
    global strContentSelector
    strContentSelector = ''

    # https://xs.sogou.com/chapter/9315264508_305241178432156/
    global strContentPageAddr
    strContentPageAddr = ''

    global strNovelName
    strNovelName = ''

def getCorrectString(str, step):
    if step == 1:
        while True:
            result = ''
            strTemp = input(str)
            response = requests.get(strTemp)
            response.encoding = response.apparent_encoding
            print(response.text)
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return strTemp
    elif step == 2:
        while True:
            result = ''
            strTemp = input(str)
            response = requests.get(strMuluAddr)
            response.encoding = response.apparent_encoding
            doc = pq(response.text)
            links = doc(strTemp)
            for link in links.items():
                print(link.attr('href'))
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return strTemp
    elif (step == 3) or (step == 4):
        while True:
            strTemp = input(str)
            if input("请确认你的输入? (y/n) : ").lower() == 'y':
                return strTemp
    elif step == 5:
        while True:
            result = ''
            strTemp = input(str)
            response = requests.get(strContentPageAddr)
            response.encoding = response.apparent_encoding
            doc = pq(response.text)
            print(doc(strTemp).text())
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return strTemp
    elif step == 6:
        while True:
            result = ''
            strTemp = input(str)
            response = requests.get(strContentPageAddr)
            response.encoding = response.apparent_encoding
            doc = pq(response.text)
            print(doc(strTemp).text())
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return strTemp
    elif step == 7:
        while True:
            strTemp = input(str)
            if input("请确认你的输入? (y/n) : ").lower() == 'y':
                return strTemp

if __name__ == "__main__":
    _init()
    strMuluAddr = getCorrectString("请输入小说目录页所在网址: ", 1)
    strLinkSelector = getCorrectString("请输入小说页Selector: ", 2)
    strPrefixAddr = getCorrectString("请输入正文网址前缀：", 3)
    strContentPageAddr = getCorrectString("请输入随意一个章节网址：", 4)
    strTitleSelector = getCorrectString("请输入标题Selector: ", 5)
    strContentSelector = getCorrectString("请输入正文Selector: ", 6)
    strNovelName = getCorrectString('请输入小说名称，用于文件名.txt: ', 7)

    print('小说下载中．．．．．．')

    #  从小说目录页遍历所有页面链接
    response = requests.get(strMuluAddr)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)

    links = doc(strLinkSelector)
    for link in links.items():
        response = requests.get(strPrefixAddr + link.attr('href'))
        response.encoding = response.apparent_encoding
        doc = pq(response.text)
        title = doc(strTitleSelector).text()
        content = doc(strContentSelector).text()

        # 使用上下文管理器打开文件
        with open(strNovelName + '.txt', mode='a+', encoding='utf-8') as f:
            f.write(title)
            f.write(content)
            f.write('')

    print('小说下载完毕!')

exit()


#  从小说目录页 http://www.jianlaixiaoshuo.com/ 获取所有页面链接
# response = requests.get('http://www.jianlaixiaoshuo.com/')
# response.encoding = response.apparent_encoding
# doc = pq(response.text)
#
# links = doc('dl > dd a')
# for link in links.items():
#     # print("http://www.jianlaixiaoshuo.com" + link.attr('href'))
#     response = requests.get("http://www.jianlaixiaoshuo.com" + link.attr('href'))
#     response.encoding = response.apparent_encoding
#     doc = pq(response.text)
#     title = doc('#BookCon > h1').text()
#     content = doc('#BookText').text()

    # # 使用上下文管理器打开文件
    # with open('剑来.txt', mode='a+', encoding='utf-8') as f:
    #     f.write(title)
    #     f.write(content)
    #     f.write('/n')


y

