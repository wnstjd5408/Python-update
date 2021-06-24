from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time


baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색학 태그를 입력하세요 :')
url = baseurl + quote_plus(plusurl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = bs(html, 'html.parser')

insta = soup.select('.v1Nh3.kIKUG._bz0w')


print(insta[0])
n = 1
for i in insta:
    print('https://www.instagram.com'+i.a['href'])
    imgurl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgurl) as f:
        with open('./img/' + plusurl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgurl)

    print()

driver.close()
