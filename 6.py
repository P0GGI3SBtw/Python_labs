##### Zadanie 6
# Utwórz dwie funkcje, które sprawdzą czy
# dany wyraz jest palindromem (wyrażenie brzmiące tak samo czytane od strony lewej
# do prawej i od prawej do lewej np. kajak)
# czy 2 dane wyrazy są anagramami (burza, arbuz)

def palindrom(word):
    i = 1
    j = len(word)
    if i < j:
        if word[i] == word[j]:
            i += 1
            j += 1
        else:
            print('wyraz nie jest palindomem')
    else:
        print('wyraz jest palindomem')


word = input('Podaj wyraz: ')

palindrom(word)