import bs4
from bs4 import BeautifulSoup
import requests
contents=requests.get("https://en.wikipedia.org/wiki/India").text
print(contents)
soup = BeautifulSoup(contents, "lxml")
#for tag in soup.findAll(True):
  #print(tag)
#for img in soup.findAll("img"):
#    print(img['src'])
for tbl in soup.findAll("table"):
    print(tbl)