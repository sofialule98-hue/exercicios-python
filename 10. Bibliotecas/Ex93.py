# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = {}
partidas = []
aproveitamento['Nome_do_Jogador'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {aproveitamento["Nome_do_Jogador"]} jogou? '))
for i in range(total):
    partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
aproveitamento['Gols'] = partidas[:]
aproveitamento['Total']= sum(partidas)
print('-' * 30)
print(aproveitamento)
print('-' * 30)
for k, v in aproveitamento.items():
    k_formatada = k.replace('_',' ')
    print(f'{k_formatada} = {v}')
print('-' * 30)
print(f'O jogador {aproveitamento["Nome_do_Jogador"]} jogou {len(aproveitamento["Gols"])} partidas.')
for i, v in enumerate(partidas):
    print(f'Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {aproveitamento["Total"]} gols.')