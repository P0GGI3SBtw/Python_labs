# Zadanie 2
# Ze strony Instytutu Informatyki z ogłoszeń dla studentów pobrać i zapisać
# wszystkie pliki typu pdf oraz wszystkie znalezione adresy url.

import requests
import bs4

url = 'https://iist.uwb.edu.pl/nii/?post_type=nowosci'

url_lst = []

codeHTML = requests.get(url, verify=True).text
print(codeHTML)

soup = bs4.BeautifulSoup(codeHTML, 'html.parser')

# Title of website
print(soup.title)

print(list(tag.name for tag in soup.find_all(True)))

while True:
    print(soup.find_all('div')[1])
    break
