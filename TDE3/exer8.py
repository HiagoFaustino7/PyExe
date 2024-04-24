# 8o Exercício
# Faça um programa em Python para calcular a soma e a média de n números
# inteiros inseridos pelo usuário. Digite 0 para terminar.

div = 0
soma = 0
x = -1

print("Digite 0 para encerrar o programa caso queira.")

while x != 0:
    x = int(input("Digite um número: "))
    soma = soma + x
    div = div + 1

print(f"A soma é: {soma} \nA média é: {soma / (div - 1)}")

