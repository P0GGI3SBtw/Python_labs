# # Zadanie 1

# # a) bez obsługi błędów
# result = 0
# while True:
#     dzialanie = input("Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Odejmowanie\nTwoj wybor: ")
#     if dzialanie == "1" or dzialanie == "2":
#         a = int(input("Podaj pierwsza liczbe: "))
#         b = int(input("Podaj druga liczbe: "))
#         if dzialanie == "1":
#             result = int(a) + int(b)
#         elif dzialanie == "2":
#             result = int(a) - int(b)
#     else:
#         print("Podaj prawidlowa wartosc")
#         continue
#
#     print("Wynik dzialania to: {}".format(result))
#     break

# b) z obsługą błędów
# result = 0
# while True:
#     dzialanie = input("Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Dzielenie\nTwoj wybor: ")
#     if dzialanie == "1" or dzialanie == "2":
#         try:
#             a = int(input("Podaj pierwsza liczbe: "))
#             b = int(input("Podaj druga liczbe: "))
#             if dzialanie == "1":
#                 result = int(a) + int(b)
#             elif dzialanie == "2":
#                 try:
#                     result = int(a) / int(b)
#                 except ZeroDivisionError:
#                     print("Nie można dzielić przez zero!")
#                     continue
#         except ValueError:
#             print("Została podana nielegalna wartość")
#             continue
#     else:
#         print("Podaj prawidlowa wartosc")
#         continue
#
#     print("Wynik dzialania to: {}".format(result))
#     break

# # Zadanie 2
# a)

# def kalkulator():
#     while True:
#         dzialanie = pobierzWartoscOdUsera(
#             "Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Dzielenie\nTwoj wybor: ")
#         if czyWartoscJestPoprawna(dzialanie):
#
#             a = int(pobierzWartoscOdUsera("Podaj pierwsza liczbe: "))
#             b = int(pobierzWartoscOdUsera('Podaj drugą liczbe: '))
#
#             przetworzDzialanie(dzialanie, a, b)
#             break
#
#
# def czyWartoscJestPoprawna(dzialanie):
#     if dzialanie == "1" or dzialanie == "2":
#         return True
#     else:
#         return False
#
#
# def przetworzDzialanie(dzialanie, a, b):
#     result = 0
#     if dzialanie == "1":
#         dodawanie = lambda a, b: a + b
#         result = dodawanie(a, b)
#     elif dzialanie == "2":
#         result = dzielenie(a, b)
#
#     wypiszWynik(result)
#
#
# def wypiszWynik(result):
#     print("Wynik dzialania to: {}".format(result))
#
#
# def pobierzWartoscOdUsera(msg):
#     return input(msg)
#
#
# def dzielenie(a, b):
#     return a / b
#
#
# kalkulator()

# b)

# def kalkulator():
#     while True:
#         dzialanie = pobierzWartoscOdUsera(
#             "Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Dzielenie\nTwoj wybor: ")
#         if czyWartoscJestPoprawna(dzialanie):
#             try:
#                 a = int(pobierzWartoscOdUsera("Podaj pierwsza liczbe: "))
#                 b = int(pobierzWartoscOdUsera('Podaj drugą liczbe: '))
#             except ValueError as e:
#                 print('Podano nieprawidłową wartość ', e)
#                 continue
#             przetworzDzialanie(dzialanie, a, b)
#             break
#
#
# def czyWartoscJestPoprawna(dzialanie):
#     if dzialanie == "1" or dzialanie == "2":
#         return True
#     else:
#         return False
#
#
# def przetworzDzialanie(dzialanie, a, b):
#     result = 0
#     if dzialanie == "1":
#         dodawanie = lambda a, b: a + b
#         result = dodawanie(a, b)
#     elif dzialanie == "2":
#         result = dzielenie(a, b)
#
#     wypiszWynik(result)
#
#
# def wypiszWynik(result):
#     print("Wynik dzialania to: {}".format(result))
#
#
# def pobierzWartoscOdUsera(msg):
#     return input(msg)
#
#
# def dzielenie(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('Nie można dzielić przez 0')
#
#
# kalkulator()


# Zadanie 3
# a)

# class Kalkulator():
#     def __init__(self):
#         pass
#
#     def uruchom(self):
#         while True:
#             dzialanie = self.pobierzWartoscOdUsera(
#                 "Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Dzielenie\nTwoj wybor: ")
#             if self.czyWartoscJestPoprawna(dzialanie):
#                 a = int(self.pobierzWartoscOdUsera("Podaj pierwsza liczbe: "))
#                 b = int(self.pobierzWartoscOdUsera('Podaj drugą liczbe: '))
#                 self.przetworzDzialanie(dzialanie, a, b)
#                 break
#
#     def czyWartoscJestPoprawna(self, dzialanie):
#         if dzialanie == "1" or dzialanie == "2":
#             return True
#         else:
#             return False
#
#     def przetworzDzialanie(self, dzialanie, a, b):
#         result = 0
#         if dzialanie == "1":
#             dodawanie = lambda a, b: a + b
#             result = dodawanie(a, b)
#         elif dzialanie == "2":
#             result = self.dzielenie(a, b)
#
#         self.wypiszWynik(result)
#
#     def wypiszWynik(self, result):
#         print("Wynik dzialania to: {}".format(result))
#
#     def pobierzWartoscOdUsera(self, msg):
#         return input(msg)
#
#     def dzielenie(self, a, b):
#         return a / b
#
#
# kalkulator = Kalkulator()
# kalkulator.uruchom()

# b)
# class Kalkulator():
#     def __init__(self):
#         pass
#
#     def uruchom(self):
#         while True:
#             dzialanie = self.pobierzWartoscOdUsera(
#                 "Wybierz dzialanie ktore chcesz wykonac\n1. Dodawanie\n2. Dzielenie\nTwoj wybor: ")
#             if self.czyWartoscJestPoprawna(dzialanie):
#                 try:
#                     a = int(self.pobierzWartoscOdUsera("Podaj pierwsza liczbe: "))
#                     b = int(self.pobierzWartoscOdUsera('Podaj drugą liczbe: '))
#                 except ValueError as e:
#                     print('Podano nieprawidłową wartość ', e)
#                     continue
#                 self.przetworzDzialanie(dzialanie, a, b)
#                 break
#
#     def czyWartoscJestPoprawna(self, dzialanie):
#         if dzialanie == "1" or dzialanie == "2":
#             return True
#         else:
#             return False
#
#     def przetworzDzialanie(self, dzialanie, a, b):
#         result = 0
#         if dzialanie == "1":
#             dodawanie = lambda a, b: a + b
#             result = dodawanie(a, b)
#         elif dzialanie == "2":
#             result = self.dzielenie(a, b)
#
#         self.wypiszWynik(result)
#
#     def wypiszWynik(self, result):
#         print("Wynik dzialania to: {}".format(result))
#
#     def pobierzWartoscOdUsera(self, msg):
#         return input(msg)
#
#     def dzielenie(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             print('Nie można dzielić przez 0')
#
#
# kalkulator = Kalkulator()
# kalkulator.uruchom()

# Zadanie 4
from tkinter import *


# def wyliczWynik():
#     wynikDzialania = 0
#     if var.get() == 1:
#         wynikDzialania = int(firstNumberTextArea.get()) + int(secondNumberTextArea.get())
#     if var.get() == 2:
#         wynikDzialania = round(int(firstNumberTextArea.get()) / int(secondNumberTextArea.get()), 2)
#
#     wynikDzialania = "Wynik działania to: " + str(wynikDzialania)
#     wynikLabel.config(text=wynikDzialania)
#
#
# mainWindow = Tk()
# var = IntVar()
# mainWindow.title("Kalkulator")
# mainWindow.geometry("400x300")
#
# labelFirstNumber = Label(mainWindow, text="Wpisz pierwszą liczbę: ")
# labelFirstNumber.grid(row=1, column=1)
# labelSecondNumber = Label(mainWindow, text="Wpisz drugą liczbę: ")
# labelSecondNumber.grid(row=2, column=1)
#
# firstNumberTextArea = Entry(mainWindow)
# firstNumberTextArea.grid(row=1, column=2)
# secondNumberTextArea = Entry(mainWindow)
# secondNumberTextArea.grid(row=2, column=2)
#
# dodawanieRB = Radiobutton(mainWindow, text=" + ", variable=var, value=1)
# dodawanieRB.grid(row=3, column=1)
# dzielenieRB = Radiobutton(mainWindow, text=" / ", variable=var, value=2)
# dzielenieRB.grid(row=4, column=1)
#
# wynikLabel = Label(mainWindow, text="")
# wynikLabel.grid(row=3, column=2)
# okButton = Button(mainWindow, text="Ok", command=wyliczWynik, fg="green")
# okButton.grid(row=4, column=2)
#
# mainWindow.mainloop()
