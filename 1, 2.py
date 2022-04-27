import os


def change_dir():
    while True:
        os.chdir(user_dir)
        print(os.listdir())
        break

actually_dir = os.listdir()

print('Bieżący katalog dyskowy: {}'.format(actually_dir))
print('Aktualna ścieżka katalogu: {}'.format(os.getcwd()))

user_dir = input('Podaj ścieżkę katalogu, który chcesz sprawdzić: ')

change_dir()
