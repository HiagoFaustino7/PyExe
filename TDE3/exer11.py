# 11o Exercício
# Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3
# valores a, b e c. Se o valor de i é par então calcular e imprimir na tela a média
# aritmética de a, b e c. Caso contrário, se i >10 então calcular e imprimir na tela a
# média aritmética e ponderada de a, b e c. Os pesos dos valores são
# respectivamente 2, 3 e 4.

i = int(input("Digite um valor: "))
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
soma = 0

if i % 2 == 0 and i < 10:
    soma = (a + b + c) / 3
else:
    soma = ((a*2) + (b*3) + (c*4)) / 9

print(soma)