# 5. Tradutor Simples:
# Desenvolva um programa que atue como um tradutor simples entre duas línguas. O
# programa deve usar um dicionário onde as chaves são palavras em uma língua e os
# valores são suas traduções em outra língua. O usuário deve poder fornecer uma
# palavra como entrada e obter sua tradução como saída.

dic = {'peixe': 'fish',
       'bola': 'ball',
       'gato': 'cat'}

while True:
    trad = input('Digite peixe, bola ou gato (ou "sair" para encerrar): ').lower()

    if trad == "sair":
        break

    traducao = dic.get(trad, "Palavra não encontrada no dicionário.")
    print(f"A tradução é: {traducao}")
