# beautiful soup 4
import bs4
from bs4 import BeautifulSoup
import requests
# contents = requests.get("https://en.wikipedia.org/wiki/India").text
# print(contents)
# soup = BeautifulSoup(contents, "lxml")
# for tag in soup.findAll(True):
#     print(tag)
# print(soup.title)
# print(soup.body)
# for img in soup.findAll("img"):
#      print(img['src'])

Link = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population"
print(Link)
data = requests.get(Link).text
# print(data)
soup1 = BeautifulSoup(data,"lxml")
# print(soup1)
print(soup1.title)
for tbl in soup1.findAll("table"):
    print(tbl)
set([tag.name for tag in soup1.findAll(True)])
for tag in soup1.findAll(True):
    print(tag.name)


