import os
import pandas as pd


class Plik:
    """
    Klasa obsługuje podany przez użytkownika plik
    ...
    Atrybuty
    --------
    nazwa : str
        nazwa pliku, który będzie edytowany
    sciezka : str
        ścieżka do pliku, który będzie obsługiwany
    tekst : str
        tekst który, będzie się znajdował w pliku

    Metody
    ------
    zapis_tekstu(sciezka, tekst):
        nawiguje plik do edycji, za pomocą ścieżki, a następnie wstawia
        zmienną tekst do pliku
    """
    licznik = 0

    def __init__(self, nazwa, sciezka, tekst):
        self.nazwa = nazwa
        self.sciezka = sciezka
        self.tekst = tekst

        Plik.licznik += 1


    def zapis_tekstu(self):
        file = open(str(self.sciezka), 'w')
        file.write(self.tekst)
        file.close()


class PlikTabela(Plik):
    def __init__(self, nazwa, sciezka, tekst, nr_kolumny, liczba_n):
        super(PlikTabela, self).__init__(nazwa, sciezka, tekst)
        self.nr_kolumny = nr_kolumny
        self.liczba_n = liczba_n


    def sumuj_dane(self):
        """
        Funkcja tworzy słownik z kolumn, dla których można wyliczyć sumę
        otwiera plik excel i zczytuje dane
        jeśli podane n jest większe od liczby rekordów w kolumnie, zwraca sumę rekordów
        w innym wypadku wyświetla stosowny komunikat
        Parametry
        ---------
            (nazwa, sciezka, tekst) - dziedziny od klasy rodzic Plik
            nr_kolumny : int
                numer kolumny, której sumę chcemy sprawdzić
            liczba_n : int
                dopuszczalna liczba rekordów w kolumnie
        """
        suma_danych = 0

        columns_dict = {1: 'A', 2: 'PassengerId', 3: 'Survived', 4: 'Pclass', 5: 'Age', 6: 'SibSp', 7: 'Parch', 8: 'Fara'}

        os.chdir('excel')
        data = pd.read_excel('titanic_copy.xlsx')

        if data.shape[0] < self.liczba_n:
            for i in range(data.shape[0]):
                suma_danych += data.loc[i, columns_dict[self.nr_kolumny]]
        else:
            print('Liczba rekordów w kolumnie jest większa od podanego n')

        print(suma_danych)



print('Ścieżka dostępu do pliku main:', os.getcwd())

o_nazwa = input('Podaj nazwę pliku: ')
o_sciezka = input('Podaj ścieżkę dostępu do pliku: ')
o_tekst = input('Podaj tekst, który chcesz tam umieścić: ')

plik1 = Plik(o_nazwa, o_sciezka, o_tekst)
plik1.zapis_tekstu()

print('Kolumny dla których można obliczyć sumę danych: \n1: A, 2: PassengerId, 3: Survived, 4: Pclass, 5: Age, 6: SibSp, 7: Parch, 8: Fara')
o_nr_kolumny = int(input('Podaj numer kolumny: '))
o_liczna_n = int(input('Podaj maksymalną liczbę rekordów w kolumnie: '))

plik2 = PlikTabela(o_nazwa, o_sciezka, o_tekst, o_nr_kolumny, o_liczna_n)
plik2.sumuj_dane()

print('Liczba utworzonych obiektów:', Plik.licznik)
