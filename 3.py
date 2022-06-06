# Zadanie 3
# Mini Bot:
# poziom 1 ze strony www http://wyborcza.pl wczytaj i zapisz do listy wszystkie znalezione adresy url
# poziom 2 wejdź na stronę www pierwszą z listy poziomu 1 sparsuj ją i
# pobierz wszystkie adresy url dostępne na tej stronie i zapisz do listy
# poziom 3 wejdź na stronę www pierwszą z listy poziomu 3 sparsuj ją i
# pobierz wszystkie adresy url dostępne na tej stronie i zapisz do listy
# Wyświetl adresy url znalezione na kolejnych poziomach'  # jeśli chcesz ustaw inną ścieżkę
# for link in adres_list_pdf:
#   url_file_split = os.path.split(link) # wynik to 2 elementowa krotka: (fragment adresu url, nazwa pliku)
#   fileName = url_file_split[1]  # nazwa pliku
# path_file_join = os.path.join(os.path.dirname(path), fileName)# połącz ścieżkę folderu i nazwe pliku
# urllib.request.urlretrieve(link, path_file_join)  # zapisz każdy dokument pdf na dysk
# Wyświetl adresy url znalezione na kolejnych poziomach

import requests
import bs4

url = 'https://wyborcza.pl/0,0.html'

codeHTML = requests.get(url, verify=True).text
print(codeHTML)

soup = bs4.BeautifulSoup(codeHTML, 'html.parser')

# Title of website
print(soup.title)

lst_link = list(link.get('href') for link in soup.find_all('a'))

f_lst_link = list(filter(None, lst_link))  # Filter non type elements
print(f_lst_link)
