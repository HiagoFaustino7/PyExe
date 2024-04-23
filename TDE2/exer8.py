# 8. Faça um
# # programa usando o for que peça uma nota, entre zero e dez. Mostre uma
# # mensagem caso o valor seja inválido e continue pedindo até que o usuário
# # informe um valor válido.





for _ in range(999999):
    nota = float(input("Digite sua nota, entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        print(f"Nota válida: {nota}")
        break
    else:
        print('Nota invalida!')

