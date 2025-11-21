import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup=BeautifulSoup(website_html, "html.parser")
allmovies=soup.find_all(name="h3", class_="title")
movie_titles=[movie.get_text()for movie in allmovies]
#movie_titles.reverse()
new_movie_titles=movie_titles[::-1]
try:
    with open("movies2.txt", "w", encoding="utf-8") as file:
        for title in new_movie_titles:
            file.write(f"{title}\n")
        print("Successfully saved all movies to movies2.txt")
        print(f"Total movies processed: {len(movie_titles)}")
except Exception as e:
    print(f"An error occurred: {e}")


