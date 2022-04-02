##### Zadanie 1

# Utwórz funkcję, która doda dwie liczby x i y, gdy trzecia podana liczba z będzie liczbą parzystą
# w przypadku gdy z jest liczbą nieparzystą wykona odejmowanie. Zadanie wykonaj w 2-ch wariantach:

# a) z - zmienna lokalna funkcji

def add_or_sub(*args):
    if define_action % 2 == 0:
        result_add = x + y
        print(result_add)
    else:
        result_sub = x - y
        print(result_sub)

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))

define_action = int(input('Podaj liczbe, jeżeli chcesz dodawać wpisz parzystą, a jeśli odejmować nieparzystą: '))

add_or_sub(x, y, define_action)

# b) z - zmienna globalna funkcji

define_action = 2

def add_or_sub(*args):
    global define_action

    if define_action % 2 == 0:
        result_add = x + y
        print(result_add)
    else:
        result_sub = x - y
        print(result_sub)

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))

add_or_sub(x, y, define_action)
