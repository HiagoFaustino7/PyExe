# 2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
# quantos valores diferentes existem na lista.


lista = []

for i in range(4):
    numero = float(input('Digite um valor:'))
    lista.append(numero)

vd = set(lista)

print(vd)




