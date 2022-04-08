from functions.info2 import *
from functions import globals as gl

gl.imie = imie = 'Jan'
gl.nazwisko = nazwisko = 'Kowalski'

lat = input('Podaj wiek: ')
mieszka = input('Podaj miejsce zamieszkania: ')
zonaty = input('Żonaty?: ')
karany = input('Podaj czy osoba była karana: ')

personal_data(imie, nazwisko, lat, mieszka, zonaty, karany)

if zonaty == 'tak':
    imie_zony = input('Podaj imię żony: ')
    nazwisko_zony = input('Podaj nazwisko żony: ')
    liczba_dzieci = int(input('Podaj liczbę dzieci: '))

    lst_dzieci = []

    ## INFO
    # for i in range(liczba_dzieci):
    #     dzicko = input('Podaj imię dziecka: ')
    #     lst_dzieci.append(dzicko)
    #     i += 1

    ## INFO 2

    

    family_data(imie_zony, nazwisko_zony, liczba_dzieci, lst_dzieci)
else:
    pass
