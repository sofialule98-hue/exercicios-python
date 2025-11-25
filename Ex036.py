# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$"))
salario_comprador = float(input("Digite seu salário: R$"))
anos_pagamento = int(input("Digite em quantos anos pretende pagar: "))

prestacao = valor_casa / (anos_pagamento * 12)

if prestacao >= salario_comprador * 0.3:
    print("Salário incompatível com o valor do imóvel. Por favor, selecione um imóvel com um valor inferior.")
else:
    print(f"Parabéns! Você está prestes a adquirir um imóvel de R${valor_casa:.2f}\n"
          f"Você irá pagar R${prestacao:.2f} por apenas {anos_pagamento} anos.")