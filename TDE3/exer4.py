# 4o Exercício
# Crie um programa em Linguagem Python que solicite a senha de um usuário e
# depois, peça para digitar novamente até que as duas senhas sejam
# correspondentes.

usuario = input("Digite o seu usuário: ")
senha = input("Digite sua senha: ")
csenha = input("Confirme a senha: ")

while senha != csenha:
    csenha = input("A senha não é igual a anterior, digite novamente: ")

print("Cadastro finalizado")

