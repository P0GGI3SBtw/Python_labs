def personal_data(imie, nazwisko, lat, mieszka, zonaty, karany):
    """
    :parameter
        globalne:
            imię (str)
            nazwisko (str)
        lokalne:
            lat (int)
            mieszka (str)
            zonaty (str)
            karny (str)
    :return
        Zdanie wypełnione zmiennymi (str i int)
    """
    print(f'Imie: {imie}, nazwisko: {nazwisko}, lat: {lat}, mieszka: {mieszka} '
          f'zonaty: {zonaty}, karany: {karany}')


def family_data(imie_zony, nazwisko_zony, liczba_dzieci, lst_dzieci):
    """
    :parameter
        lokalne:
            imie_zony (str)
            nazwisko_zony (str)
            liczba_dzieci (int)
    :return
        Zdanie wypełnione zmiennymi (str i int)
    """
    print(f'Imie żony: {imie_zony}, nazwisko żony: {nazwisko_zony}, '
          f'liczba dzieci: {liczba_dzieci}, imiona dzieci: {lst_dzieci}')
