# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter
jogos = {'Jogador 1': randint(1, 6),
              'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True) # a função itemgetter irá dar prioridade para a chave indicada invés de seguir da primeira chave em diante
print('-' * 27)
print(f'{"== RANKING DOS JOGADORES ==":^27}')
print('-' * 27)
for k, v in enumerate(ranking):
    print(f'{k + 1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1.3)
