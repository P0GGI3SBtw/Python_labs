## FUNCTIONS FOR MAIN:

def authors(number_of_authors):
    lst_authors = []

    if number_of_authors > 1:
        for i in range(number_of_authors):
            author = input('Podaj autora: ')
            lst_authors.append(author)
        return lst_authors
    elif number_of_authors == 1:
        author = input('Podaj autora: ')
        return author


def toms(number_of_toms):
    lst_toms = []

    if number_of_toms > 1:
        for i in range(number_of_toms):
            tom = input('Podaj nazwe tomu: ')
            lst_toms.append(tom)
        print(f'Tomy: {lst_toms}')
        pass

    elif number_of_toms == 1:
        tom = input('Podaj nazwe tomu: ')
        print(f'Tom: {tom}')
        pass

    elif number_of_toms == 0:
        print('Brak tomów')
        pass
