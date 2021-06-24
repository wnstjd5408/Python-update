from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time


baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plueurl = input('검색어를 입력해주세요 : ')

url = baseurl + quote_plus(plueurl)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


naver = soup.select('_image')

print(naver[0])
