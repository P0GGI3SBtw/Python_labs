import requests
import bs4
import time

url = 'https://www.olx.pl/d/oferta/rolex-gmt-master-ii-rozowe-zloto-nowy-126715chnr-rok-2022-CID87-IDORREm.html'

codeHTML = requests.get(url, verify=True).text
# print(codeHTML)

soup = bs4.BeautifulSoup(codeHTML, 'html.parser')

# Title of website
print(soup.title)

list(tag.name for tag in soup.find_all(True))

while True:
    print(soup.find_all('h3')[0])
    time.sleep(5)
