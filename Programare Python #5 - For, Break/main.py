# Sectiunea 1
# lista_fructe = ['mere', 'banane', 'portocale', 'cirese']
#
# for fruct in lista_fructe:
#     print(fruct)


# Sectiunea 2
# lista_fructe = ['mere', 'banane', 'portocale', 'cirese']
#
# for i in range(len(lista_fructe)):
#     lista_fructe[i]='mere'
#
# print(lista_fructe)


# Sectiunea 3
# for i in range(0, 101, 2):
#     print(i)


# Sectiunea 4
# note = [5, 7, 6, 4, 9, 10]
#
# suma = 0
#
# for i in range(len(note)):
#     suma += note[i]
#
# media = round(suma / len(note), 2)
#
# print(media)


# Sectiunea 5
# numere = [6, 7, 3, 1, 10]
#
# produs = 1
#
# for i in range(len(numere)):
#     produs *= numere[i]
#
# print(produs)


# Sectiunea 6
# note = [5, 7, 6, 4, 9, 10]
#
# for nota in note:
#     if nota <= 4:
#         print("nota insuficienta")
#         break
#     print(nota)


# Sectiunea 7
# import random
#
# print(round(random.random() * 1000))
#
# print(random.randint(10, 250))
#
# numere = [6, 4, 18, 9, 10]
# print(random.choice(numere))
#
# random.shuffle(numere)
# print(numere)


# Sectiunea 8
# import random
#
# litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#           'u', 'v', 'w', 'x', 'y', 'z']
# cifre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# simboluri = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#              '_', '-', '+', '=', ':', ';', "'", '"', '<', ',',
#              '>', '.', '/', '?'
#              ]
#
# caractere_parola = []
#
# for i in range(5):
#     caractere_parola.append(random.choice(litere))
#
# for i in range(2):
#     caractere_parola.append(random.choice(cifre))
#
# for i in range(2):
#     caractere_parola.append(random.choice(simboluri))
#
# random.shuffle(caractere_parola)
#
# parola = ''
#
# for caracter in caractere_parola:
#     parola+=caracter
#
# print(parola)
#
