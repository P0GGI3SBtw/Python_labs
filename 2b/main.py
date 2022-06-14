from functions.operatory import *

user_input = input('Podaj liczbe lub liczby: ')

n_list = user_input.split()

if len(n_list) > 3:
    print('Suma podanych liczb wynosi:', suma(n_list))
elif len(n_list) <= 3:
    print('Iloczyn podanych liczb wynosi:', iloczyn(n_list))
