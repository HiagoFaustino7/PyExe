# 8. Frequência de Letras:
# Crie um programa que receba uma string como entrada e conte o número de
# ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O
# programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
# valores são o número de vezes que cada letra ocorre na string.
texto = input("Digite uma string: ")


def contar_letras(texto):
    # Inicializa um dicionário vazio para armazenar as contagens
    contagem_letras = {}

    # Converte o texto para minúsculas para garantir que não haja distinção entre maiúsculas e minúsculas
    texto = texto.lower()

    # Itera sobre cada caractere no texto
    for caractere in texto:
        # Verifica se o caractere é uma letra do alfabeto
        if caractere.isalpha():
            # Se o caractere já estiver no dicionário, incrementa o contador
            if caractere in contagem_letras:
                contagem_letras[caractere] += 1
            # Caso contrário, adiciona o caractere ao dicionário com contagem 1
            else:
                contagem_letras[caractere] = 1

    return contagem_letras

# Recebe uma string como entrada do usuário

# Chama a função para contar as letras e armazena o resultado em um dicionário
resultado = contar_letras(texto)

# Imprime o dicionário de contagem de letras
print("Contagem de letras:")
for letra, contagem in resultado.items():
    print(f"{letra}: {contagem}")
