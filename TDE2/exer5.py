# 5.Crie um programa que leia o conceito de um aluno na disciplina Desenv Web 3
# e imprima seu significado, de acordo com a tabela abaixo. Caso seja informado um
# conceito inexistente, deve ser exibida uma mensagem de erro.
# Conceito Significado
# A Excelente
# B Ótimo
# C Bom
# D Regular
# E Ruim
# F Nos vemos de novo ano que vem...

sig = {'A': 'Excelente',
       'B': 'Ótimo',
       'C': 'Bom',
       'D': 'Regular',
       'E': 'Ruim',
       'F': 'Nos vemos de novo ano que vem'}

nota = input('Digite sua nota: ').upper()

while nota not in ['A', 'B','C', 'D', 'E', 'F']:
    nota = input('!!@@!!ERRO!!@@!!\n Nota inválida, digite novamente: ')

print(sig[nota])
