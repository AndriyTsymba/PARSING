##4
import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content , "html.parser")
    for script in soup.find_all("style","script"):
        script.extract()# вирізаємо непотріб
    text = " ".join(soup.stripped_strings)
    worlds = len(text.split())
    print(worlds)