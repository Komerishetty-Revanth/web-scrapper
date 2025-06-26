import requests
from bs4 import BeautifulSoup
URL = 'https://www.bbc.com/news'
response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f"Failed to load page: {URL}")
soup = BeautifulSoup(response.content, 'html.parser')
headlines = []

for h in soup.find_all(['h1', 'h2', 'h3']):
    text = h.get_text(strip=True)
    if text and len(text.split()) > 2:  
        headlines.append(text)
with open("headlines.txt", "w", encoding="utf-8") as file:
    for idx, title in enumerate(headlines, start=1):
        file.write(f"{idx}. {title}\n")

print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")
