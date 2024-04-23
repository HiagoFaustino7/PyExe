# 3. Uma loja fornece 10% de desconto para funcionários e 5% de desconto para
# clientes vips. Faça um programa usando while que calcule o valor total a ser
# pago por uma pessoa. O programa deverá ler o valor total da compra
# efetuada e um código que identifique se o comprador é um cliente comum (1)
# , funcionário (2) ou vip(3) .

v = float(input("Digite o valor total da compra: "))
c = int(input("Digite seu código: [1] = cliente [2] = funcionario  [3] = vip: "))



while c not in [1,2,3]:
    c = int(input("Codigo invalido, digite novamente: [1] = cliente [2] = funcionario  [3] = vip: "))

if c == 2:
    v = v * 0.90
elif c == 3:
    v = v * 0.95

print(f"O valor total da sua compra é: {v}")

