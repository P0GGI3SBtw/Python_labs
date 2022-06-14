from functions.operatory import *

user_input = input('Podaj liczbe lub liczby: ')

n_list = user_input.split()

if len(n_list) == 1:
    n = int(n_list[0])
    if n % 2 == 0:
        print('Sinus podanej liczby wynosi:', sinus(n))
    else:
        print('Potenga podanej liczby wynosi:', potenga(n))
else:
    print('Iloczyn podanych liczb wynosi:', iloczyn(n_list))
