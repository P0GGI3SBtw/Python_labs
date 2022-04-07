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
<<<<<<< HEAD
        lokalne:
            imie_zony (str)
            nazwisko_zony (str)
            liczba_dzieci (int)
    :return
        Zdanie wypełnione zmiennymi (str i int)
    """
    print(f'Imie żony: {imie_zony}, nazwisko żony: {nazwisko_zony}, '
          f'liczba dzieci: {liczba_dzieci}, imiona dzieci: {lst_dzieci}')
=======
        zonaty (str)
        imie żony (str)
        nazwisko żony (str)
        liczna dzieci (int)
    :return
        Jeśli jest zonaty, to pyta, o żone oraz dzieci i ich imiona,
        a jeśli nie to nic nie wykonuje
    """

    if zonaty == 'tak':
        imie_zony = input('Podaj imie żony: ')
        nazwisko_zony = input('Podaj nazwisko żony: ')
        liczba_dzieci = int(input('Podaj liczbe dzieci: '))

        list_dzieci = []

        for i in range(liczba_dzieci):
            imie_dziecka = input('Podaj imie dziecka: ')
            list_dzieci.append(imie_dziecka)

        print(f'Imie żony: {imie_zony}, nazwisko żony: {nazwisko_zony}, '
              f'liczba dzieci: {liczba_dzieci}, imona dzieci: {list_dzieci}')
    else:
        pass
    
>>>>>>> 7b92f1d9e791434cf5c1aa991e09289c5c04b9fd
