#  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#  e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 16)
print("- BANCO PYTHON -")
print("=" * 16)
valor = int(input("Qual será o valor a ser sacado? R$"))
total = valor # cópia do valor para ir diminuindo
ced = 50 # começa verificando com a maior cédula (R$50)
total_ced = 0
while True:
    if total >= ced: # se o valor total for maior ou igual ao valor da cédula
        total -= ced # é subtraído o valor da cédula do total
        total_ced += 1 # e contabilizado + 1 cédula deste valor
    else:
        # não cabe mais cédulas deste valor
        # mostra quantas cédulas deste valor foram usadas (se tiver alguma)
        if total_ced > 0: # se o total de cédulas for maior que zero
            print(f"Total de {total_ced} cédulas de R${ced:.2f}")
        # muda para a próxima cédula (menor valor)
        if ced == 50: # se o valor da cédula for 50, passa a valer 20
            ced = 20
        elif ced == 20: # se o valor da cédula for 20, passa a valer 10
            ced = 10
        elif ced == 10: # se o valor da cédula for 10, passa a valer 1
            ced = 1
        total_ced = 0 # zera o contador para começar a contar as novas cédulas
        if total == 0: # se o total for igual a zero o programa para e mostra a quantidade de cada cédula utilizada para chegar no valor inputado pelo usuário
            break
print("-" * 30)
print("Volte Sempre ao BANCO PYTHON!")
