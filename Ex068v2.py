# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
from time import sleep
cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input("Digite um valor: "))
    soma = computador + jogador
    tipo = ''
    while True:
        entrada = str(input("Par ou Ímpar? ")).strip().upper()
        if entrada == 'P' or entrada == 'I':
            tipo = entrada
            break
        elif entrada == 'PAR':
            tipo = 'P'
            break
        elif entrada == 'IMPAR' or entrada == 'ÍMPAR':
            tipo == 'I'
            break
        else:
            print("Por favor, digite P para Par ou I para ímpar.")
    print(f"Você jogou {jogador} e o computador jogou {computador}. A soma dos valores é igual a {soma}.", end=' ')
    print("Deu PAR!" if soma % 2 == 0 else "Deu ÍMPAR!" )
    sleep(1.5)
    if tipo == 'P':
        if soma % 2 == 0:
            print("VOCÊ VENCEU!")
            cont += 1
        else:
            print("VOCÊ PERDEU!")
            break
    if tipo == 'I':
        if soma % 2 != 0:
            print("VOCÊ VENCEU!")
            cont += 1
        else:
            print("VOCÊ PERDEU!")
            break
    print('Vamos jogar novamente...')
print(f"GAME OVER!\n"
      f"Você venceu {cont} vezes.")

