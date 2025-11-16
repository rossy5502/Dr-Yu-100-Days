import requests
from bs4 import BeautifulSoup

#year=input("what year would you like to travel to yyyy-mm-dd:")
header={"User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
       "Safari/537.36 Edg/142.0.0.0"}
#URL=f"https://www.billboard.com/charts/hot-100/{year}"
url2="https://www.billboard.com/charts/hot-100/"
response=requests.get(url2)
response.raise_for_status()
web_page_content=response.text
soup=BeautifulSoup(web_page_content, "html.parser")
#song_title = soup.select("li h3.c-title")
song_title=soup.find_all("h3",id="title-of-a-story")

song_lists =[]
for song in song_title:
    print(song.get_text(strip=True))

