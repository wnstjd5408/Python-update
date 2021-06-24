import requests
from bs4 import BeautifulSoup


html = requests.get(
    "https://movie.naver.com/movie/bi/mi/basic.nhn?code=196051")
# print(html)
movie_soup = BeautifulSoup(html.text, "html.parser")
# print(movie_soup)

data1 = movie_soup.find("div", {"class": "sub_tab_area"})


things = data1.find('a', {'class': 'tab01 on'}).text

print('첫번째 : ' + things)


data2 = movie_soup.find('div', {"class": "story_area"})


content = data2.find('p', {'class': 'con_tx'}).text


print('내용 :' + content)


# links = data1.find_all('a')
# # print(li)

# li_name = []
# for a in links:
#     li_name.append(links.find('em').string)


# li_name = li_name[0:5]
# print(li_name)
