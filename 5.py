###############Zadanie 5
# Utwórz funkcję tabliczka(x1, x2, y1, y2), która wypisze na ekran tabliczkę
# mnożenia dla liczb [x1, . . . , x2] × [y1, . . . , y2];
#
# x = range(1, 4) N
# y = range(6, 10) M
#
# N x M
# 6, 12, 18
# 7, 14, 21
# 8, 16, 24
# 9, 18, 27

def sub_tab(x):
    result = 0

    for i in range(3):
        result = result + x
        print(result)

x = int(input('Podaj liczbe: '))

sub_tab(x)