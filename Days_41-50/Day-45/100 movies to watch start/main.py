import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.encoding = 'utf-8'  # Ensure proper encoding
web_page_content = response.text
soup=BeautifulSoup(web_page_content, "html.parser")
title_data = soup.find_all('h3', class_='title')

results=[]
for title in title_data:
    text = title.text.strip()
    
    # Clean the text (replace special dashes with regular hyphens)
    text = text.replace('–', '-').replace('—', '-')
    
    # Extract position and title using a more specific pattern
    # This looks for a number at the start, followed by ) or :, then the title
    match = re.match(r'^(\d+)(?:\)|:)\s*(.+)$', text)
    if not match:
        # Try alternative patterns if the first one doesn't match
        match = re.match(r'^(\d+)\s*[)\-\.]\s*(.+)$', text)
    
    if match:
        position = match.group(1).strip()
        title_text = match.group(2).strip()
        results.append((int(position), title_text))
# Sort by position to ensure correct order
results.sort()
print(results)

try:
    with open("movies.txt", "w", encoding='utf-8') as file:
        for position, title in results:
            file.write(f"{position}) {title}\n")
    print("Successfully saved all movies to movies.txt")
    print(f"Total movies processed: {len(results)}")
except Exception as e:
    print(f"An error occurred: {e}")













