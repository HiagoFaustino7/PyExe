# 8. Frequência de Letras:
# Crie um programa que receba uma string como entrada e conte o número de
# ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O
# programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
# valores são o número de vezes que cada letra ocorre na string.

idades = []
alturas = []

def linha():
  print('-'*30)


n = int(input('Quer ver a altura e idade de quantas pessoas? '))

for i in range(n):
  linha()
  idade = int(input(f'Digite sua idade Nº {i+1}: '))
  altura = float(input(f'Digite a altura da pessoa Nº {i+1}: '))
  linha()
  idades.append(idade)
  alturas.append(altura)


while n not in [0]:
  n -= 1
  print(f"Idade = {idades[n]}, Altura = {alturas[n]} metros")