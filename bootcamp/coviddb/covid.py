import requests
from bs4 import BeautifulSoup

ref = requests.get(url="https://www.ndtv.com/coronavirus/india-covid-19-tracker")

soup = BeautifulSoup(ref.content, features="html.parser")
cases = soup.find_all("p", class_="mid-wrap")
states = soup.find_all("label")
fh = open("covid_data.csv", "w")

j = 0
for i in states[:-2]:
    fh.write(i.get_text())
    fh.write(",")
    for k in range(4):
        try:

            if k != 1:
                numbers = cases[j].get_text().split(" ")
                for h in numbers:
                    if h == "":
                        fh.write("0")
                        fh.write(",")
                    else:
                        fh.write(h)
                        fh.write(",")
            else:
                element = cases[j].get_text().split(" ")
                fh.write(element[0])
                fh.write(",")
            j += 1
        except:
            break
    fh.write("\n")

fh.close()
