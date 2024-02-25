from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

article_tags = soup.find_all('span', class_='titleline')
article_texts = []
article_links = []
article_upvotes = []

for tag in article_tags:
    article_texts.append(tag.get_text())
    article_links.append(tag.a['href'])

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_ ="score")]

max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)

print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])