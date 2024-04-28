# 3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
# No final mostre:
# a)Quantas vezes apareceu o valor 9.
# b)Em que posição foi digitado o primeiro valor 3.
# c)Quais foram os números pares.

lista = []
nove = 0
pos = 0
pares = []

for i in range(4):
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n == 9:
        nove += 1
    if pos == 0 and n == 3:
        pos = i + 1
    if n % 2 == 0:
        pares.append(n)
print(f"O valor 9 apareceu {nove} vezes.")
if pos > 0:
    print(f"O valor 3 apareceu pela primeira vez na posição {pos}.")
else:
    print("O valor 3 não foi digitado.")
print(f"Números pares digitados: {pares}")

