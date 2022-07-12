# Sectiunea 1
# zile_saptamana = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
# i=0
# while i<4:
#     print(f"Saptamana {i}: ", end="")
#     j=0
#     while j<7:
#         print(zile_saptamana[j],end=",")
#         j=j+1
#     print()
#     i=i+1


# Sectiunea 2
# while True:
#     a = int(input("Introduceti primul numar: "))
#     b = int(input("Introduceti al doilea numar: "))
#     print("Rezultatul adunarii este: ", a + b)
#     print("Rezultatul scaderii este: ", a - b)
#     print("Rezultatul inmultirii este: ", a * b)
#     print("Rezultatul impartirii este: ", a / b)
#     continua = input("Doriti sa continuati? (y/n) ")
#     if continua == "n":
#         break


# Sectiunea 3
# propozitie = input("Introduceti propozitia: ")
# vocale = ['a', 'e', 'i', 'o', 'u']
# nr_vocale = 0
# i=0
# while i < len(propozitie):
#     if propozitie[i] in vocale:
#         nr_vocale += 1
#     i += 1
# print()
# print(f"Propozitia contine {nr_vocale} vocale")


# Sectiunea 4
# import random
#
# lista_numere = []
#
# i = 0
# while i < 10:
#     lista_numere.append(random.randint(1, 100))
#     i += 1
#
# i = 0
# nr_pare = 0
# suma_pare = 0
# while i < len(lista_numere):
#     if lista_numere[i] % 2 == 0:
#         nr_pare += 1
#         suma_pare += lista_numere[i]
#     i += 1
#
# print(lista_numere)
# print(f"Media numerelor pare este {suma_pare/nr_pare}")


# Sectiunea 5
# lista_numere = [4, 10, 2, 5, 8, 12]
# s = 0
# i = 0
# while i<len(lista_numere):
#     s = s+lista_numere[i]
#     i = i + 1
# print(s)


# Sectiunea 6
# import random
#
# while True:
#     print("\nOptiuni: \n1.Piatra\n2.Hartie\n3.Foarfeca")
#     optiuni_disponibile = ["Piatra","Hartie","Foarfeca"]
#
#     utilizator = int(input("Alegerea dumneavoastra: "))
#     calculator = random.randint(1,3)
#
#     alegere_utilizator = optiuni_disponibile[utilizator-1]
#     alegere_calculator = optiuni_disponibile[calculator-1]
#
#     print(f"Utilizatorul a ales {alegere_utilizator}")
#     print(f"Calculatorul a ales {alegere_calculator}")
#
#     if alegere_utilizator == alegere_calculator:
#         print("Egalitate")
#     elif alegere_utilizator == "Piatra" and alegere_calculator == "Hartie":
#         print("Calculatorul a castigat")
#     elif alegere_utilizator == "Foarfeca" and alegere_calculator =="Hartie":
#         print("Utilizatorul a castigat")
#     elif alegere_utilizator == "Foarfeca" and alegere_calculator == "Piatra":
#         print("Calculatorul a castigat")
#     elif alegere_utilizator == "Hartie" and alegere_calculator == "Piatra":
#         print("Utilizatorul a castigat")
#     elif alegere_utilizator == "Hartie" and alegere_calculator == "Foarfeca":
#         print("Calculatorul a castigat")
#     elif alegere_utilizator =="Piatra" and alegere_calculator == "Foarfeca":
#         print("Utilizatorul a castigat")
#     else:
#         print("Valoarea introdusa nu este valida")
#
#     print()
#     r = input("Doriti sa mai jucati? (y/n): ")
#     if r == "n":
#         break