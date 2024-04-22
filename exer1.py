# 1. Escreva um programa que receba 2 números de sua escolha e que depois
# imprima a soma, a subtração, multiplicação, divisão, divisão inteira, o resto da
# divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de
# símbolo %..

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

sub = x - y
mul = x * y
divI = x // y
div = x / y
res = 0
if x > y:
    res = x % y
else:
    res = y % x

print(f"SUBTRAÇÃO: {sub}")
print(f"MULTIPLICAÇÃO: {mul}")
print(f"DIVISÃO: {div}")
print(f"DIVISÃO INTEIRA: {divI}")
print(f"RESTO MAIOR PELO MENOR: {res}")








