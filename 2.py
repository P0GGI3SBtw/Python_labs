def search_word(word, *args):
       if word in text:
              print('Podane słowo znajduje sie w tekście')
       else:
              print('Podane słowo nie znajduje się w tekście')

       for word in args:
              if word in text:
                     print('Podane słowo znajduje sie w tekście')
              else:
                     print('Podane słowo nie znajduje się w tekście')

text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest ' \
       'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
       'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu.' \
       'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać' \
       'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie' \
       'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe' \
       'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym' \
       'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie' \
       'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do' \
       'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'

search_word('port', 'komputer', 'xD')