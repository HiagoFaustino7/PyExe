# 10. Faça um programa usando o for que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

menor = 9999999999999
maior = 0
soma = 0


n = int(input("Digite a quantidade total de números do programa: "))

for i in range (n):
    num = float(input("Digite um número: "))
    soma = soma + num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num


print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma de todos: {soma}")
