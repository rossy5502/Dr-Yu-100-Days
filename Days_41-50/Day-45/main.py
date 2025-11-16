from bs4 import BeautifulSoup
import lxml, requests

url="https://news.ycombinator.com/news"
response=requests.get(url)
web_page_content=response.text
soup=BeautifulSoup(web_page_content, "html.parser")
title_spans = soup.find_all('span', class_='titleline')
results = []

for span in title_spans:
    a_tag = span.find('a')
    title = a_tag.text
    href = a_tag['href']
    #score_span = span.parent.parent.find_next_sibling('tr').find('span', class_='score')
    score_span=soup.find(name="span", class_="score")
    score = int(score_span.text.split()[0]) if score_span else 0
    results.append({'title': title, 'href': href, 'score': score})

# Find the entry with the highest score
if results:
    top = None
    for result in results:
        if not top or result['score'] > top['score']:
            top = result
    print(f"Top Title: {top['title']}")
    print(f"Top Score: {top['score']}")
    print(f"Top Href: {top['href']}")
else:
    print("No results found.")






