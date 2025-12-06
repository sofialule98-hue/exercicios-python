# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print("JOGO DE ADIVINHAÇÃO \n")

computador = randint(0, 5) # a função randint irá sortear entre os números inteiros estabelecidos
jogador = int(input("Escolhi um número entre 0 e 5, qual o seu palpite? "))

if jogador == computador:
    print(f"Correto! O número que escolhi foi {jogador}.")
elif jogador > 5:
    print("Tente um número menor! O jogo funciona de 0 a 5.")
else:
    print("Você errou! Tente novamente.")

