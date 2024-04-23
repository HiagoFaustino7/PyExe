# 6. Dada uma letra, escreva na tela se essa letra é uma vogal ou consoante
# (considerar apenas letras minúsculas).

letra = input('Digite uma letra: ').lower()


if letra.isalpha() and len(letra) == 1:

    if letra in 'aeiou':
        print('É uma vogal')

    else:
        print('É uma consoante')


else:

    print('Você digitou mais de uma letra, ou algum número, renicie o programa.')
