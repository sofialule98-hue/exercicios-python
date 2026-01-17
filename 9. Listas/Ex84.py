# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Por favor, digite S para sim e N para não. Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print('-' * 15)
print(f'{"- RESULTADOS: -":^15}')
print('-' * 15)
print(f'Pessoas cadastradas: {len(pessoas)}')
print('Pessoa mais pesadas: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} com {maior}Kg.')
print('Pessoa mais leves: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} com {menor}Kg.')


