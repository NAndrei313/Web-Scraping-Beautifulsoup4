import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

movie_title = [title.getText().replace("â\x80\x93", "-") for title in soup.find_all(name="h3", class_="title")]
movies = movie_title[::-1]
movies[84] = "85) Leon"
# print(movies)

with open("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
