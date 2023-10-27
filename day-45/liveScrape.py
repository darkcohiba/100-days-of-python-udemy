import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.scrapethissite.com/pages/simple/")
response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# finding the first article
# article_title = soup.find(name='a', rel='noreferrer').string
# article_link = soup.find(name='a', rel='noreferrer').get('href')
# article_upvote = soup.find(name='span', class_='score').string
# print(f"title: {article_title}\n"
#       f"link: {article_link}\n"
#       f"votes: {article_upvote}")


# doing all the articles
articles = soup.select('.titleline > a:first-child')
# print(articles)
articles_upvotes = [int(score.string.split(' ')[0]) for score in soup.find_all(name='span', class_='score')]
article_list = []

for index, article in enumerate(articles):
    art_obj = {
        "title": article.string,
        "link": article.get('href'),
        "upvotes": articles_upvotes[index]
    }
    article_list.append(art_obj)


# print(article_list)
sorted_article_list = sorted(article_list, key=lambda x: x['upvotes'], reverse=True)
print(sorted_article_list)
# print(articles_upvotes)

