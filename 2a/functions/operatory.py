"""
    Moduł posiada funkcję wykorzystujące liczbę/liczby n i wykonują na nich poszczególne operacje (potęgowanie, sinus z n, iloczyn liczb)
"""

from math import sin


def potenga(n):
    return n ** 2


def sinus(n):
    return round(sin(n), 2)


def iloczyn(n_list):
    wynik = 1

    for i in range(len(n_list)):
        wynik *= int(n_list[i])

    return wynik
