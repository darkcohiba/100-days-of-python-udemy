import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.scrapethissite.com/pages/simple/")
response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup.title)