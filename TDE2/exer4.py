# 4. Dado o valor do produto e a forma de pagamento.
# 1= à vista;
# 2= à prazo.
# Se o produto for pago à vista aplique um desconto de 10% antes de mostrar
# o valor final, senão informe o mesmo valor do produto.

v = float(input("Digite o valor: "))

produto = int(input("O valor foi pago a vista? [1] para sim, [0] para não: "))

if produto == 1:
    v = v * 0.90
else:
    v = v

print(f"O valor do produto final é: {v}")
