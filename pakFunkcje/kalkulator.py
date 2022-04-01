import math

def iloczyn(pierwszaLiczba, drugaLiczba):
    result = pierwszaLiczba * drugaLiczba
    return result

def iloraz(pierwszaLiczba, drugaLiczba):
    while True:
        try:
            if drugaLiczba == 0:
                print('Nie można dzielić przez 0')
                break
            else:
                result = pierwszaLiczba / drugaLiczba
                return result
            break
        except ValueError:
            print('To nie jest cyfra')

def silnia(x):
    result = math.factorial(x)
    return result