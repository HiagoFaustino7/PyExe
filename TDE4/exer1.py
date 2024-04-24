# 1. Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado(entre 0 e 20) e mostrá-la por extenso.

n_e = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n= int(input("Digite um número entre 0 e 20: "))
if 0 <= n <= 20:
    print(f"O número {n} por extenso é: {n_e[n]}")
else:
    print("Número fora do intervalo permitido.")




