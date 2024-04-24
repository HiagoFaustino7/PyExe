# 4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
# lista. Faça um programa que determine o percentual de ocorrências de face 6 do
# dado dentre esses 50 lançamentos.



import random
lista = []
green = 0
for i in range(0, 50):
    dado = random.randint(1, 6)
    lista.append(dado)
    if dado == 6:
        green = green + 1
print(f"Apareceu o dado 6: {green} vezes = {100* (green / 50):.2f}% das vezes")