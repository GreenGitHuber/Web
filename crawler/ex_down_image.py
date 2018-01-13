#首先找到要下载的东西在哪里
#1、使用requests库下载
#2、使用beautifulsoup来处理网页如何用正则表达式表示
#3、然后再用requests下载图片
from bs4 import BeautifulSoup
import requests
import re

URL = "http://www.nationalgeographic.com.cn/index.php?m=content&c=index&a=lists&catid=596"
html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')

#在soup中找到带有
img_ul = soup.find_all('dl',{'class':'show-list-dl aside-box'})
for ul in img_ul:
    imgs = ul.find_all('img',{'src':re.compile("^http://")})
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
