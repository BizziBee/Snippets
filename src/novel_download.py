#
#

import requests
from pyquery import PyQuery as pq


def _init():
    # https://xs.sogou.com/list/9315264508
    global strMuluAddr
    strMuluAddr = ''

    # True: 目录是正常顺序; False: 目录是反序
    global boolOrder
    boolOrder = False

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
            str_temp = input(str)
            response_ = requests.get(str_temp)
            response_.encoding = response_.apparent_encoding
            print(response_.text)
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return str_temp
    elif step == 2:
        while True:
            result = ''
            str_temp = input(str)
            response_ = requests.get(strMuluAddr)
            response_.encoding = response_.apparent_encoding
            query_doc = pq(response_.text)
            query_links = query_doc(str_temp)
            for query_link in query_links.items():
                print(query_link.attr('href'))
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return str_temp
    elif (step == 3) or (step == 4):
        while True:
            str_temp = input(str)
            if input("请确认你的输入? (y/n) : ").lower() == 'y':
                return str_temp
    elif step == 5:
        while True:
            result = ''
            str_temp = input(str)
            response_ = requests.get(strContentPageAddr)
            response_.encoding = response_.apparent_encoding
            query_doc = pq(response_.text)
            print(query_doc(str_temp).text())
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return str_temp
    elif step == 6:
        while True:
            result = ''
            str_temp = input(str)
            response_ = requests.get(strContentPageAddr)
            response_.encoding = response_.apparent_encoding
            query_doc = pq(response_.text)
            print(query_doc(str_temp).text())
            if input("是否是你要的结果? (y/n) : ").lower() == 'y':
                return str_temp
    elif step == 7:
        while True:
            str_temp = input(str)
            if input("请确认你的输入? (y/n) : ").lower() == 'y':
                return str_temp
    elif step == 8:
        while True:
            str_temp = input(str)
            if input("请确认你的输入? (y/n) : ").lower() == 'y':
                return str_temp


if __name__ == "__main__":
    _init()
    strMuluAddr = getCorrectString("请输入小说目录页所在网址: ", 1)
    strLinkSelector = getCorrectString("请输入目录页Selector: ", 2)
    tmp = getCorrectString("目录是否是正序吗 (y/n) : ", 8)
    if tmp[0].lower() == 'y':
        boolOrder = True
    else:
        boolOrder = False
    strPrefixAddr = getCorrectString("请输入正文网址前缀：", 3)
    strContentPageAddr = getCorrectString("请输入随意一个章节网址：", 4)
    strTitleSelector = getCorrectString("请输入标题Selector: ", 5)
    strContentSelector = getCorrectString("请输入正文Selector: ", 6)
    strNovelName = getCorrectString('请输入小说名称，用于文件名.txt: ', 7)

    print('小说下载中．．．．．．')

    #  从小说目录页遍历所有页面链接
    response = requests.get(strMuluAddr)
    response.encoding = response.apparent_encoding
    response_doc = pq(response.text)
    links = response_doc(strLinkSelector)

    lstTmp = []
    for link in links.items():
        lstTmp.append(strPrefixAddr + link.attr('href'))

    if not boolOrder:
        lstTmp.reverse()

    for link in lstTmp:
        response = requests.get(link)
        response.encoding = response.apparent_encoding
        response_doc = pq(response.text)
        title = response_doc(strTitleSelector).text()
        content = response_doc(strContentSelector).text()

        # 使用上下文管理器打开文件
        with open(strNovelName + '.txt', mode='a+', encoding='utf-8') as f:
            f.write(title)
            f.write(content)
            f.write('\r\n')

    print('小说下载完毕!')

exit()

#  从小说目录页 http://www.jianlaixiaoshuo.com/ 获取所有页面链接
# response = requests.get('http://www.jianlaixiaoshuo.com/')
# response.encoding = response.apparent_encoding
# pqdoc = pq(response.text)
#
# links = pqdoc('dl > dd a')
# for link in links.items():
#     # print("http://www.jianlaixiaoshuo.com" + link.attr('href'))
#     response = requests.get("http://www.jianlaixiaoshuo.com" + link.attr('href'))
#     response.encoding = response.apparent_encoding
#     pqdoc = pq(response.text)
#     title = pqdoc('#BookCon > h1').text()
#     content = pqdoc('#BookText').text()

# # 使用上下文管理器打开文件
# with open('剑来.txt', mode='a+', encoding='utf-8') as f:
#     f.write(title)
#     f.write(content)
#     f.write('/n')


y
