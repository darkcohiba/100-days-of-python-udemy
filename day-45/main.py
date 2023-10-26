from bs4 import BeautifulSoup


with open('website.html') as web_file:
    contents = web_file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)