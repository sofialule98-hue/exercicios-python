# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
import  sys
from time import sleep

print("=" * 20)
print("VAMOS JOGAR JOKENPÔ!")
print("=" * 20)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


jogador = int(input("Suas opções: \n"
                    "[ 0 ] PEDRA \n"
                    "[ 1 ] PAPEL \n"
                    "[ 2 ] TESOURA \n"
                    "Qual é a sua jogada? "))

if jogador > 2: # inclui esta condição para que o usuário tenha um retorno caso coloque um número inválido para o jogo.
    print("Opção deve estar entre 0 e 2! Tente novamente.")
    sys.exit()


print('-=' * 15)
print(f"Você escolheu {itens[jogador]}.")
print(f"O computador escolheu {itens[computador]}.")
print('-=' * 15)

sleep(1.2)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("VOCÊ VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("VOCÊ VENCEU!")
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print("VOCÊ VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
print("Melhor de 3? :)")
