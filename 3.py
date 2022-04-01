### Manual
def averange(*args):
    result = sum(args) / len(args)
    print(result)

averange(1, 2, 3, 4, 5, 6)

### Automatic
lst = []

def averange(*args):
    result = sum(lst) / number_digits
    print(result)

number_digits = int(input('Ile cyfr chesz podać: '))

for n in range(number_digits):
    numbers = int(input('Podaj liczbe: '))
    lst.append(numbers)

averange(lst, number_digits)