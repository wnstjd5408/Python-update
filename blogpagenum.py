import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://cafe.naver.com/fitthesize?iframe_url=/ArticleList.nhn%3Fsearch.clubid=29942898%26search.menuid=54%26search.boardtype=I"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

data1 = soup.select('album-img')

print(data1[0])


driver.close()
