from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
img = soup.select('.tile_item._item')
print(img[0])

n = 1
for i in img:
    imgUrl = i.select_one('.thumb').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/image' + plusUrl + str(n)+'.jpg', 'wb') as h:  # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()


print('다운로드 완료')
