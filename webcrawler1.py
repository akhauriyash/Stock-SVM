import requests
from bs4 import BeautifulSoup


def spider(maxpage):
    page = 1
    while page <= maxpage:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        sourcecode = requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
            print(href)
        page +=1


spider(1)