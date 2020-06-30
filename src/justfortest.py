
import requests
import os

# url = "http://n.sinaimg.cn/news/crawl/146/w550h396/20200630/308c-ivrxcex6422127.png"
url = 'http://img0-lemall.letvimg.com/le-cloud/resource/images/video/20190114/zero65.mp4'
root = "c://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已保存')
except:
    print('爬取失败')
