# 9. Faça um programa usando o for que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações.

for _ in range(999999999):
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome == senha:
        print("O nome de usuario não pode ser igual a senha.")
    else:
        break