# # Zadanie 5
# a)
# import unittest as ut
#
#
# class Test_calculator(ut.TestCase):
#     def test_1(self):
#         while True:
#             dzialanie = "2"
#             if dzialanie == "1" or dzialanie == "2":
#                 a = 2
#                 b = 3
#             if dzialanie == "1":
#                 result = int(a) + int(b)
#                 self.assertEqual(result, 5, 'Powinno być 5')
#             elif dzialanie == "2":
#                 result = int(a) - int(b)
#                 self.assertEqual(result, -1, 'Powinno być -1')
#             else:
#                 print("Podaj prawidłowa wartość")
#                 continue
#
#             print("Wynik dzialania to: {}".format(result))
#             break

# b)
# import unittest as ut
#
#
# class Test_calculator(ut.TestCase):
#     def test_2(self):
#         def kalkulator():
#             while True:
#                 dzialanie = "1"
#                 if czyWartoscJestPoprawna(dzialanie):
#                     a = 1
#                     b = 3
#                     przetworzDzialanie(dzialanie, a, b)
#                     break
#
#
#         def czyWartoscJestPoprawna(dzialanie):
#             if dzialanie == "1" or dzialanie == "2":
#                 return True
#             else:
#                 return False
#
#
#         def przetworzDzialanie(dzialanie, a, b):
#             result = 0
#             if dzialanie == "1":
#                 dodawanie = lambda a, b: a + b
#                 result = dodawanie(a, b)
#                 self.assertEqual(result, 4, 'Powinno byc 4')
#             elif dzialanie == "2":
#                 result = dzielenie(a, b)
#
#             wypiszWynik(result)
#
#
#         def wypiszWynik(result):
#             print("Wynik dzialania to: {}".format(result))
#
#
#         def dzielenie(a, b):
#             return a / b
#
#
#         kalkulator()
