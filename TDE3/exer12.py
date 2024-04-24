# 12o Exercício
# Escreva um programa em Python para calcular o número fatorial de qualquer
# número.

n, f = int(input("Digite um número para calcular o fatorial: ")), 1

for i in range(1, n + 1):
    f *= i
print(f"O fatorial de {n} é {f}.")
