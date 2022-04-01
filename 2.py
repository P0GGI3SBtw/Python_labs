# Zadanie 2
# a) Utwórz w folderze roboczym skrypt modkalkulator.py który będzie modułem
# w tym skrypcie utwórz funkcje suma, która wykona dodawanie dwóch liczb
# b) przestestuj swój funkcję, utwórz w folderze roboczym kolejny skrypt o nazwie mainLab4.py
# który będzie zawierał natępujący kod:
#

import modkalkulator
pierwszaLiczba = int(input("Wpisz pierwszą liczbę: "))
drugaLiczba = int(input("Wpisz drugą liczbę: "))
print('Suma liczb:',pierwszaLiczba,'+',drugaLiczba, \
'wynosi:',modkalkulator.suma(pierwszaLiczba,drugaLiczba))