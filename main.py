from task import *

#### Zadanie 1

# a)
print('Solution 1:')
print(set_gene1.intersection(set_gene2, set_gene3))

# b)
print('Solution 2:')
print(set_gene1.difference(set_gene2))

# c)
print('Solutin 3:')
print(set_gene1.difference(set_gene2, set_gene3))

#### Zadanie 2

if 'FGFR4' in lista_gene1:
  index_1 = lista_gene1.index('FGFR4')
  print(index_1)
if 'FGERA4' in lista_gene1:
  index_2 = lista_gene1.index('FGERA4')
  print(index_2)
else:
  print('Gen nie znajduje sie w liscie')


#### Zadanie 3

# a)
result_a = txt.count('Emma')
print(result_a)

# b)
result_b = txt.upper()
print(result_b)

# c)
list_c = ['Emma', 'AI']
print(list_c)

# d)
result_d = txt.count('.')
print(result_d)

#### Zadanie 4

x = int(input('Podaj x: '))

if x % 2 == 0:
  print(f'Podana liczba {x} jest przysta')
else:
  print(f'Podana liczba {x} nie jest przysta')

#### Zadanie 5

n = int(input("Podaj n: "))

result = 0

for i in range(1, n+1):
  result += 1 / i

print(result)

#### Zadanie 7

import math
n = 10

while(n > 0):
  print(math.sqrt(n))
  n -= 1

####################################################################################
####################################################################################

#### Zadanie 1

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))

while(x > 0 and y > 0):
  result = x * y
  print(result)
  break

#### Zadanie 2

password = '1234'

user_input = input('Podaj hasło: ')

if user_input == password:
  print('Szymon Kołodziejski')
else:
  print('Podane hasło jest nieprawidłowe')

#### Zadanie 3

list_3 = [21, 4, 75, 33, 94, 12, 85, 22, 11, 85]

for i in list_3:
  if i % 2 == 0:
    print(i)

list_3.sort()
print(list_3)

import random

print(random.sample(list_3, 3))
print(random.choice(list_3))

### Zadanie 4

password = '1234'

user_input = input('Podaj hasło: ')

print('Szymon Kołodziejski') if user_input == password else print('Podane hasło jest nieprawidłowe')

#### Zadanie 5

def odd_mult(list):
  mult = 1

  for number in list:
    if number % 2 != 0:
      mult *= number

  return mult

list = [1, 3, 12, 16, 23, 17, 24]

print(odd_mult(list))
