def shop(branza, ilosc_pracownikow, dzień, ilosc_towaru, **kwargs):
    print(f'branża: {branza}')
    print(f'Ilość pracowników: {ilosc_pracownikow}')
    print(f'Dzień: {dzień}')
    print(f'Ilość towaru: {ilosc_towaru}')
    print()

shop('IT', 14, 1, 22)
shop('Medicine', 33, 1, 394)