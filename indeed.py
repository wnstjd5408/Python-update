import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div",  {"class":  "pagination"})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.text))

    max_pages = pages[-1]

    return max_pages


def extract_indeed_jobs(last_pages):
    jobs = []
    # for page in range(last_pages):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "tapItem"})
    for result in results:
        title = result.find("div", {"class": "heading4"}).text
        company = result.find("span", {"class":  "companyName"}).text
        print(company)
    return jobs
