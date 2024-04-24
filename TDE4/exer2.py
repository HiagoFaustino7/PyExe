# 2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
# quantos valores diferentes existem na lista.

lista = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    lista.append(valor)


v_u = set(lista)
print(len(v_u))




