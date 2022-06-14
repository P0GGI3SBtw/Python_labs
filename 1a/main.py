import os


class Prostopadloscian:
    """
    Klasa wylicza obszary prostopadłościanu.
    ...
    Atrybuty
    --------
    a : int
        pierwsza bok podstawy prostopadłościanu
    b : int
        drugi bok podstawy prostopadłościanu
    h : int
        wysokość prostopadłościanu

    Metody
    ------
    pole_powierzchni_bocznej(a, b, h):
        zwraca wynik: pole powierzchni bocznej prostopadłościanu,
        o podanych parametrach
    pole_podstawy(a, b):
        zwraca wynik: pole podstawy prostopadłościanu,
        o podanych parametrach
    """
    licznik = 0

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

        Prostopadloscian.licznik += 1

    def pole_powierzchni_bocznej(self):
        """
        Zwraca pole powierzchni bocznej prostopadłościanu,
        o podanych parametrach
        Parametry
        ---------
            a : int
                pierwsza bok podstawy prostopadłościanu
            b : int
                drugi bok podstawy prostopadłościanu
            h : int
                wysokość prostopadłościanu
        """
        return 2 * (self.a * self.h) + 2 * (self.b * self.h)

    def pole_podstawy(self):
        """
        Zwraca pole podstawy prostopadłościanu,
        o podanych parametrach
        Parametry
        ---------
            a : int
                pierwsza bok podstawy prostopadłościanu
            b : int
                drugi bok podstawy prostopadłościanu
        """
        return self.a * self.b


class Szescian(Prostopadloscian):
    def __init__(self, *args):
        super(Szescian, self).__init__(*args)


    def pole_powierzchni(self):
        return 6 * (self.a ** 2)

x = int(input('Podaj a: '))
y = int(input('Podaj b: '))
high = int(input('Podaj wysokość: '))

figura1 = Prostopadloscian(x, y, high)
ppb = figura1.pole_powierzchni_bocznej()
print(ppb)
pp = figura1.pole_podstawy()
print(pp)

figura2 = Szescian(x, y, high)
ppow = figura2.pole_powierzchni()
print(ppow)


print('Liczba utworzonych obiektów:', Prostopadloscian.licznik)

### Wykorzystanie os
print('Lokalizacja pliku main:', os.getcwd())
print('Pliki w folderze:', os.listdir())

file = open('1a.txt', 'w')
file.write('Prostopadloscian:\nPole powierzchni bocznej: {}\nPole podstawy: {}\nSzescian:\nPole powierzchni: {}'.format(ppb, pp, ppow))
file.close()
