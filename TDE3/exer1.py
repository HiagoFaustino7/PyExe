# 1o Exercício
# Faça um programa em linguagem Python que lê um número n digitado pelo
# usuário(esse número vai ser a quantidade de termos) e imprima os n primeiros
# números da sequência de Fibonacci.


n = int(input("Quantos números na sequencia voce quer mostrar: "))

n1 = 0
n2 = 1
n3 = 0

for i in range (n):
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(f"-> {n3}")