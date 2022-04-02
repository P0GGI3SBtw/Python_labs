##### Zadanie 6
# Sprawdza czy dany wyraz jest palindromem (wyrażenie brzmiące tak samo
# czytane od strony lewej do prawej i od prawej do lewej np. kajak)

def palindr(word):
    x = 0
    for i in range(len(word)):
        if word[0] == word[-1]:
            x = x + 1
        else:
            x = x

    if len(word) == x:
        print('Podany wyraz jest palindorem')
    else:
        print('Podany wyraz nie jest palindorem')

word = input('Podaj wyraz, który chcesz sprawdzić: ')

palindr(word)

# Sprawdza czz 2 dane wyrazy są anagarmami, wyrazy, które powstały z tych samych liter np. (arbuz, burza)

def anagram(word1, word2):
    lst_w1 = []
    lst_w2 = []

    for i in range(len(word1)):
        lst_w1.append(i)
    lst_w1.sort()

    for i in range(len(word2)):
        lst_w2.append(i)
    lst_w2.sort()

    if lst_w1 == lst_w2:
        print('Podane wyrazy są anagramami')
    else:
        print('Podanie wyrazy nie są anagramami')

word1 = input('Podaj pierwszy wyraz: ')
word2 = input('Podaj drugi wyraz: ')

anagram(word1, word2)
