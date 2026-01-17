# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()
        if pessoa['sexo'] in 'FM':
           break
        print('Por favor, digite F para Feminino e M para Masculino.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar in 'SN':
            break
        print('Por favor, digite S para Sim e N para Não.')
    if continuar == 'N':
        break
media = soma / len(dados)
print('-' * 25)
print(f'A) Pessoas Cadastradas: {len(dados)}')
print(f'B) Média de Idade: {media:.1f} anos')
print(f'C) Mulheres Cadastradas: ', end='')
for i in dados:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print(f'\nD) Pessoas com Idade Acima da Média: ', end='')
for i in dados:
    if i['idade'] > media:
        print(f'{i["nome"]}', end=' ')
