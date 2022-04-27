import fnmatch
import os


def files(func):
    dir_task = os.listdir('Task_6')

    print('Zawartość folderu Task_6:', dir_task)

    print('Pliki z zakończenie ABC:')
    os.chdir('Task_6')

    for file in dir_task:
        if fnmatch.fnmatch(file, '*ABC'):
            print(file)
            file_open = open(file, 'r')
            file_read = file_open.read()

            words = file_read.split()
            count_words = 0

            for word in words:
                if len(word) > 2:
                    count_words += 1

            print(count_words)

    return func


@files
def files_update():
    # Already in Task_6
    dir_task = os.listdir()
    print(dir_task)

    count_file = 0

    print('Liczba słów w plikach nie zawierających 0:')

    for file in dir_task:
        if '0' in file:
            count_file += 1
        else:
            file_open = open(file, 'r').read()

            words = file_open.split()
            count_words = 0

            for word in words:
                if len(word) > 1:
                    count_words += 1

            print('{}: {}'.format(file, count_words))

    print('Liczba plików zawierających 0 w nazwie: {}'.format(count_file))


files_update()
