# 7. Crie um programa usando o for que leia uma lista. Mostre apenas os
# números pares. Esta lista deve ser assim: [1, 2, 3, 4, 5, 6, 7, 8, 9];
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in lista:
    if numero % 2 == 0:
        print(numero)

