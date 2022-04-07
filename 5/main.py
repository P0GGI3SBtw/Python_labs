from functions.mode import *

# Questions for user
print('Elementy obowiązkowe:')

number_of_authors = int(input('Podaj liczbe autorów: '))
title = input('Podaj temat pracy: ')
journal = input('Podaj czasopismo: ')
year = int(input('Podaj rok wydania: '))

# range of pages
first_page = int(input('Podaj początkową stronę: '))
last_page = int(input('Podaj ostatnia stornę: '))

if first_page > last_page:
    print('Podano zły zakres')
else:
    pass

print('Elementy opcjonalne:')

number_of_toms = int(input('Podaj liczbe tomów, z których korzystasz, jeśli nie wpisz 0: '))

# Output

print('Autorzy: ', authors(number_of_authors))
print(f'Tytuł: {title}')
print(f'Czasopismo: {journal}')
print(f'Rok wydania: {year}')
print(f'Zakres stron: {first_page} - {last_page}')
toms(number_of_toms)
