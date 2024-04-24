# 6o Exercício
# Faça um programa em Python que leia n números inteiros e positivos a partir do
# teclado, até que o usuário digite 0. Ao final, informe o maior número digitado.

x = -1
maior = 0
print("Caso queira encerrar o programa digite 0")
while x != 0:
    x = int(input("Digite um valor: "))
    if x > maior:
        maior = x

print(f"Maior número digitado: {maior}")
