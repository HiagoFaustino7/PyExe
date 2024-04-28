# 7. Escreva uma função que recebe como entrada um número inteiro positivo n e
# retorne a soma de todos os inteiros positivos menores ou iguais a n.

def soma_ate_n(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

# Teste da função
numero = int(input("Digite um número inteiro positivo: "))
resultado = soma_ate_n(numero)
print(f"A soma de todos os inteiros positivos menores ou iguais a {numero} é: {resultado}")
