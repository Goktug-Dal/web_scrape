from bs4 import BeautifulSoup
import requests

link = requests.get("https://webscraper.io/test-sites/pagination")
soup = BeautifulSoup(link.text, "html.parser")

names = soup.find_all("p", attrs = {"class": "card-text"})
#company = names.find("h3",attrs = "abc")
#more_info = name.header.h2.a
for name in names:
    print(name.text.replace('\n', ''))