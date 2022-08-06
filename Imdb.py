import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

list = soup.find('tbody', {"class": "lister-list"}).find_all('tr', limit = 5)

for tr in list:
    title = tr.find('td', {"class": "titleColumn"}).find('a').text
    year = tr.find('td', {"class": "titleColumn"}).span.text.strip('()')
    rating = tr.find('td', {"class": "ratingColumn"}).strong.text
    print(title, year, rating)
