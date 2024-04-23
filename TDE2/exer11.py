# 11.Faça um programa usando o for que calcule o número médio de alunos por
# turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para
# cada turma. As turmas não podem ter mais de 40 alunos.

max = 40
t = int(input("Digite o número de turmas: "))
x = 0
y = 0
q = 0
total = 0

for i in range (t):
    x = x + 1
    y = y + 1
    if max >= q:
        q = int(input(f"Diga a quantidade de alunos dessa turma {x}: "))
        total = total + q
    elif max <= q:
        print("As turmas não podem ter mais de 40 alunos.")
        break

if t == y:
    print(f"A média de alunos na turma é: {total / t}")
