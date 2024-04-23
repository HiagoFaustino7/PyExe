# 4. Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas e minúsculas
# b) Quantas letras ao todo
# c) Quantas letras tem o primeiro nome

nome_c = input("Digite seu nome completo: ")

nome_mai = nome_c.upper()
nome_min = nome_c.lower()

total_let = len(nome_c.replace(" ", ""))
primeiro_nome = nome_c.split()[0]
letras_pnome = len(primeiro_nome)

print(f"NOME COMPLETO: {nome_c} \n"
      f"Maiusculo: {nome_mai} \n"
      f"Minusculo: {nome_min} \n"
      f"Numero de letras: {total_let} \n"
      f"Numero letras primeiro nome: {letras_pnome} \n")


