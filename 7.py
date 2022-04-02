# ##Zadanie 7
# Zaprogramuj funkcję rzut_kostka(), która symuluje rzut sześcienną
# kością do gry, tzn. funkcja ma zwracać losową liczbę naturalną z
# przedziału [1 . . . 6]. Korzystając z tej funkcji zaprogramuj prostą
# grę (z dwoma zawodnikami), w której w każdej turze każdy zawodnik rzuca dwie
# kostki (tj. dwukrotnie wywołuje funkcję rzut_kostka()). Turę wygrywa ten, kto
# wyrzuci więcej kostek. Grę wygrywa ten, kto po n turach ma więcej zwycięstw.
# Jeśli po n turach jest remis,
#  gra toczy się do pierwszego zwycięstwa.
# Komputer ma grać sam ze sobą, po ukończonej grze program wyświetla wyniki wszystkich n-tur,
# w zadaniu wykorzystaj funkcję enumerate

import random

player_1 = []
player_2 = []

number_of_round = int(input('Podaj ile rund chcesz rozegrać: '))

def throw_a_dice():
    integer = random.randint(1, 6)
    return integer

for i in range(number_of_round):
    player_1.append(throw_a_dice())
    player_1.append(throw_a_dice())

    player_2.append(throw_a_dice())
    player_2.append(throw_a_dice())

# # Check code:
# print(player_1)
# print(player_2)
# print(sum(player_1), sum(player_2))

if sum(player_1) == sum(player_2):
    player_1.append(throw_a_dice())
    player_1.append(throw_a_dice())

    player_2.append(throw_a_dice())
    player_2.append(throw_a_dice())

    number_of_round = number_of_round + 1

elif sum(player_1) > sum(player_2):
    print('Gracz nr. 1 wygrał')
    print(f'Gra zakończyła się po {number_of_round} rundach')

elif sum(player_2) > sum(player_1):
    print('Gracz nr. 2 wygrał')
    print(f'Gra zakończyła się po {number_of_round} rundach')

print('Statystyki gracza 1:')
for i in enumerate(player_1):
    print(i)

print('Statystyki gracza 2:')
for i in enumerate(player_2):
    print(i)