
import bs4
from bs4 import BeautifulSoup
import requests
contents = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)").text
print(contents)
soup = BeautifulSoup(contents, "lxml")
for tag in soup.findAll(True):
    print(tag)
print(soup.title)
print(soup.body)
for img in soup.findAll("img"):
    print(img['src'])
