"""info.py: Mouduł zawiera funkcję do pliku main.py, pozwalające na jego obsłge"""

__name__ = 'info'
__author__ = 'Szymon Kołodziejski'
__version__ = '1.0.0'


def personal_data(imie, nazwisko, lat, mieszka, zonaty, karany):
    """
    Args:
        global:
            :param imie: (str)
            :param nazwisko: (str)
        lokal:
            :param lat: (int)
            :param mieszka: (str)
            :param zonaty: (str)
            :param karany: (str)
    Returns:
        Zdanie wypełnione zmiennymi (str, int)
    Raises:
        Zaimplementowany wyjątek zapobiega wprowadzeniu przez użytkownika innego typy zmiennej niż oczekiwana w pliku main.py
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
        :param imie_zony: (str)
        :param nazwisko_zony: (str)
        :param liczba_dzieci: (int)
        :param args: (str, list), (imiona dzieci)
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
