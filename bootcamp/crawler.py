import requests
from bs4 import BeautifulSoup

link_main = requests.get(url="https://www.metrolyrics.com/drake-overview.html")

soup = BeautifulSoup(link_main.content, features="html.parser")

links = soup.find_all("a", attrs={"class": "title"})
for i in links:
    print(i)
