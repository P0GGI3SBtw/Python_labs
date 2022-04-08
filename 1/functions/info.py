"""info.py: Mouduł zawiera funkcję do pliku main.py, pozwalające na jego obsłge"""

__name__ = 'info'
__author__ = 'Szymon Kołodziejski'
__version__ = '1.0.0'


def personal_data(imie, nazwisko, lat, mieszka, zonaty, karany):
    """
    Args:
        global:
            imię (str): imie osoby określone w main.py
            nazwisko (str): nazwisko osoby określone w main.py
        lokal:
            lat (int)
            mieszka (str)
            zonaty (str)
            karny (str)
    Returns:
        Zdanie wypełnione zmiennymi (str, int)
    Raises:
        Zaimplementowany wyjątek zapobiega wprowadzeniu przez użytkownika złego typy zmiennej w pliku main.py
    """
    while True:
        try:
            print('Imie: {}, nazwisko: {}, lat: {}, mieszka: {} zonaty: {}, karany: {}'.format(imie, nazwisko, lat,
                                                                                               mieszka, zonaty, karany))
            break
        except ValueError:
            print('Podano parametr niewłaściwego typu')


def family_data(imie_zony, nazwisko_zony, liczba_dzieci, *args):
    """
    Args:
        imie_zony (str)
        nazwisko_zony (str)
        liczba_dzieci (int)
        imiona dzieci (str, list)
    Returns:
        Zdanie wypełnione zmiennymi (str, int)
    """
    while True:
        try:
            print('Imie żony: {}, nazwisko żony: {}, '
                  'liczba dzieci: {}, imiona dzieci: {}'.format(imie_zony, nazwisko_zony, liczba_dzieci, *args))
            break
        except ValueError:
            print('Podano parametr niewłaściwego typu')
