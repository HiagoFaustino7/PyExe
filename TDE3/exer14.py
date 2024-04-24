# 14o Exercício
# Faça um programa em que o usuário informe o salário recebido e o total gasto com
# despesas. Deverá ser exibido na tela “Gastos dentro do orçamento” caso o valor
# gasto não ultrapasse o valor do salário e “Orçamento estourado” se o valor gasto
# ultrapassar o valor do salário.

s = float(input("Digite seu salário: "))
g = float(input("Digite seus gastos: "))

if g > s:
    print("Orçamento estourado")
else:
    print("Gastos no orçamento")