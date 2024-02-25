import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇
response = requests.get(URL)
top_100_movies_webpage = response.text
soup = BeautifulSoup(top_100_movies_webpage, "html.parser")

article_tags = soup.find_all("h3", class_="title")
article_list = [article.getText() for article in article_tags]

article_list.reverse()

# Write article_list to movies.txt
with open("movies.txt", "w") as file:
    for movie in article_list:
        file.write(f"{movie}\n")
