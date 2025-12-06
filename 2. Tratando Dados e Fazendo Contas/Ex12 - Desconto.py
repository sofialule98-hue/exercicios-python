# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço atual do produto: "))

desconto = preco * 0.05
novo_preco = preco - desconto

print(f"O preço do produto com 5% de desconto é igual a {novo_preco:.2f} reais.")
