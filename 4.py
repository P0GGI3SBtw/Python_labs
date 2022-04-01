##### Zadanie 4
# Utwórz w pliku kalkulator.py funkcję o nazwie silnia,
# która obliczy wartość silni dla zmiennej
# zdeklarowanej przez użytkownika.
# następnie dodaj odpowiedni kod w pliku mainLab4.py,
# który obliczy wyrażenie n!/(k!(n-k)!) wykorzystując
# możliwości pakietu pakFunkcje
# Uwaga: pamiętaj o import pakFunkcje.kalkulator

from pakFunkcje.kalkulator import silnia

x = int(input("Wpisz liczbę: "))
print(f'Silnia liczby {x}! wynosi: {silnia(x)}',)