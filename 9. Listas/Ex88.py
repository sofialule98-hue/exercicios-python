# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
lista = []
jogos = []
total = 1
palpites = int(input('Quantos jogos você quer sortear? '))
while total <= palpites:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'SORTEANDO {palpites} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i + 1}: {l}')
