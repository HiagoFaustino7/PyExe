#2. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno

n1 = float(input("Nota 1º BI:"))
n2 = float(input("Nota 2º BI: "))
n3 = float(input("Nota 3º BI:"))
n4 = float(input("Nota 4º BI:"))

med = (n1 + n2 + n3 + n4) / 4

print(f"A média é: %.1f"% med)
