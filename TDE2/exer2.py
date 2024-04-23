# 2. Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até
# 200Km e R$0,45 para viagens mais longas.


d = float(input("Digite a distância da viagem em KM: "))

if d < 201:
    print(f"O preço da viagem é: {0.50 * d}")
else:
    print(f"O preço da viagem é: {0.45 * d} R$")

