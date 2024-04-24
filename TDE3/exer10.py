# 10o Exercício
# Escreva um laço que calcule:
# a) a soma de todos os números pares entre 2 e 100(inclusive)
# b) A soma de todos os quadrados entre 1 e 100(inclusive)
# c) A soma de todos os números ímpares entre a e b
# d) A soma de todos os dígitos ímpares de n(Por exemplo, se n for 32677;.

soma = 0
soma2 = 0
soma3 = 0
soma4 = 0
a = int(input("Digite valor de A: "))
b = int(input("Digite valor de B: "))
n = int(input("Digite um numero: "))

for i in range(2, 101):
    if i % 2 == 0:
        soma = soma + i


print(f'A soma de todos os números pares entre 2 e 100(inclusive): {soma}')

for i in range(1, 101):
    soma2 = soma2 + (i*i)

print(f'A soma de todos os quadrados entre 1 e 100(inclusive): {soma2}')


for i in range(a, b + 1):
    if i % 2 != 0:
        soma3 = soma3 + i

print(f'A soma de todos os números ímpares entre a e b: {soma3}')



for _ in range(len(str(n))):
    n = n % 10
    if n % 2 != 0:
        soma4 += n
    n //= 10

print("A soma de todos os dígitos ímpares de", n, "é:", soma4)
