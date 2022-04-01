# Output wartość n-tego elementu, suma elementów ciągu
import math

def ciag_geo(*lst_agr):
    for i in range(0, n):
        current_term = a1 * math.pow(q, i)
        print(current_term)
        total = (n * (1 - math.pow(q, i - 1)))
    print(total)


n = int(input('Podaj numer elementu ciągu, który chcesz obliczyć: '))
a1 = int(input('Podaj wartość pierwszego elementu ciągu: '))
q = int(input('Podaj wartość iloczynu ciągu geometrycznego: '))

lst_agr = [n, a1, q]

ciag_geo()