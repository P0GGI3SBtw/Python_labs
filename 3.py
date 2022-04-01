### Wykonaj proste zadanie które pozwoli Ci zrozumieć jak tworzyć i korzystać z własnych pakietów
### Uwaga: Pakiety pozwalają na utrzymanie porządku w przestrzeni nazw modułów
### np. nazwa modułu X.y oznacza moduł składowy "y" pakietu "X".
##### Zadanie 3
# a) Utwórz w folderze roboczym pakiet pakFunkcje a w nim 2 pliki
# pierwszy o nazwie kalkulator.py w tym pliku utwórz dwie funkcje o nazwach iloczyn i iloraz, które
# wykonają mnożenie lub dzielenie dwóch liczb

# Możesz to wykonać na 2 sposoby: korzystając z File -> New -> Python Package  lub
# utwórz folder o nazwie pakFunkcje a w nim pusty skrypt o nazwie __init__.py  (ten plik informuje że ten folder stanowi moduł)
# b) przestestuj swój moduł, w skrypcie o nazwie mainLab4.py
# wpisz natępujący kod:

from pakFunkcje.kalkulator import iloczyn
from pakFunkcje.kalkulator import iloraz

pierwszaLiczba = int(input("Wpisz pierwszą liczbę: "))
drugaLiczba = int(input("Wpisz drugą liczbę: "))
print('Iloczyn liczb:',pierwszaLiczba,'*',drugaLiczba, \
       'wynosi: ',iloczyn(pierwszaLiczba,drugaLiczba))
print('Iloraz liczb:',pierwszaLiczba,'*',drugaLiczba, \
       'wynosi: ',iloraz(pierwszaLiczba,drugaLiczba))

