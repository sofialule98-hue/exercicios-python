# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print("=== SUPERMERCADO PYTHON ===")

total = 0
quant = quant1000 = 0
barato = 0
produto_barato = ''

while True:
    nome_produto = str(input("Produto: ")).strip()
    preco = float(input("Preço: "))
    quant += 1
    total += preco
    if preco >= 1000:
        quant1000 += 1
    if quant == 1:
        barato = preco
        produto_barato = nome_produto
    elif preco < barato:
        barato = preco
        produto_barato = nome_produto
    continuar = ''
    while continuar not in ('S', 'N'):
        entrada = str(input("Deseja continuar [S/N]? ")).strip().upper()
        if entrada and entrada[0] in 'SN':
            continuar = entrada[0]
        else:
            print("Por favor, digite S ou N.")
    if continuar == 'N':
        break
print("-" * 18)
print("RESUMO DA COMPRA:")
print("-" * 18)
print(f"Quantidade de produtos: {quant}")
print(f"Total gasto na compra: R${total:.2f}")
print(f"Quantidade de produtos com valor a cima de R$1000: {quant1000}")
if quant > 0:
    print(f"O produto comprado com menor valor foi {produto_barato} por R${barato:.2f}")
print("Volte Sempre!")
