def suma(n_list):
    """
    Funkcja oblicza sumę wszystkich elementów, podanych przez użytkownika
    Parametry
    ---------
        n_list : list
            lista elementów, podanych przez użytkownika
        i : int
            odniesienie do poszczególnego elementu listy
    Zwraca
    ------
        Wynik dodawanie wszystkich elementów listy
    """
    wynik = 0

    for i in range(len(n_list)):
        wynik += int(n_list[i])

    return wynik


def iloczyn(n_list):
    wynik = 1

    for i in range(len(n_list)):
        wynik *= int(n_list[i])

    return wynik
