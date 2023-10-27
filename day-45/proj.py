import requests
from bs4 import BeautifulSoup


url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())


movies = soup.select('.article-title-description__text .title')
movie_list = []
for movie in movies:
    movie_list.append(movie.string)


print(movie_list)
