# 9o Exercício
# Escreva um programa em Python para encontrar números entre 100 e 400 (ambos
# inclusos), onde cada dígito de um número é um número par. Os números obtidos
# devem ser impressos em sequência separada por vírgulas.


print("Números onde cada dígito é par entre 100 e 400:")
for numero in range(100, 401):
    digito_centena = numero // 100
    digito_dezena = (numero // 10) % 10
    digito_unidade = numero % 10

    if digito_centena % 2 == 0 and digito_dezena % 2 == 0 and digito_unidade % 2 == 0:
        print(numero, end=', ')
print("\b\b")

