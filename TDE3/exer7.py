# 7o Exercício
# Crie um programa em linguagem Python que permite ao usuário inserir os valores
# dos produtos comprados por um cliente. O programa deve terminar quando o
# usuário inserir o valor 0. Se o usuário digitar um valor negativo não deve ser
# processado e um novo valor deve ser solicitado como entrada. Ao final, informe o
# valor total a pagar, lembrando que, caso as vendas ultrapassem o total de R$ 1.000
# , deverá ser aplicado um desconto de 10%.


x = -1
valort = 0
while x != 0:
    valort = valort + x
    x = int(input("Digite o valor do produto: "))
    if x < 0:
        x = int(input("Digite o valor novamente: "))
        valort = valort + (x * x)

if valort > 1000:
    print(f"Valor total da compra: {valort*0.9+1} R$")
else:
    print(f"Valor total da compra: {valort+1} R$")


