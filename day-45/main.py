from bs4 import BeautifulSoup


with open('website.html') as web_file:
    contents = web_file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.li)
# print(soup.a)


# print(soup.find_all(name="li"))
# print(soup.findAll(name="li"))

all_anchor_tags = soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.string)
    print(tag.getText())
    print(tag.href)
    print(tag.get("href"))