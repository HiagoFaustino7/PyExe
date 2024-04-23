# 5o Exercício
# Faça um programa em Python que leia n números inteiros a partir do teclado, até
# que o usuário digite 0. Ao final, mostre a soma de todos os números digitados.

x = -1
soma = 0
print("Caso queira encerrar o programa digite 0")
while x != 0:
    x = int(input("Digite um valor: "))
    soma = soma + x


print(soma)