# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('-' * 19)
print("* LOJINHA PYTHON *")
print('-' * 19)

valor_produto = float(input("Digite o valor do produto: R$"))

pagamento = int(input("FORMAS DE PAGAMENTO: \n"
                      "[ 1 ] Á Vista Dinheiro/Cheque \n"
                      "[ 2 ] À Vista Cartão \n"
                      "[ 3 ] 2x Cartão \n"
                      "[ 4 ] 3x ou Mais Cartão \n"
                      "Sua opção: "))

if pagamento == 1:
    novo_valor = valor_produto - (valor_produto * 0.1)
    print(f"Lhe foi concedido 10% de desconto neste produto! Sua compra de R${valor_produto:.2f} fica por R${novo_valor:.2f}")
elif pagamento == 2:
    novo_valor = valor_produto - (valor_produto * 0.05)
    print(f"Lhe foi concedido 5% de desconto neste produto! Sua compra de R${valor_produto:.2f} fica por R${novo_valor:.2f}")
elif pagamento == 3:
    parcela = valor_produto / 2
    print(f"Esta forma de pagamento não inclui descontos ou juros. Sua compra fica por R${valor_produto:.2f} com 2 parcelas de R${parcela:.2f}")
elif pagamento == 4:
    novo_valor = valor_produto + (valor_produto * 0.2)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = novo_valor / total_parcelas
    print(f"Esta forma de pagamento inclui 20% de juros! Sua compra de R${valor_produto:.2f} fica por R${novo_valor:.2f} com {total_parcelas} parcelas de R${parcela:.2f}")
else:
    print("Forma de pagamento inválida! Tente novamente.")

print("VOLTE SEMPRE!")
