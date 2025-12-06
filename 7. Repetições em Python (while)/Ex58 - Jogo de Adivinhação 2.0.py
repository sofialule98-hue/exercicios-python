# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print("=" * 23)
print("JOGO DE ADIVINHAÇÃO 2.0")
print("=" * 23)
cont = 1 # o contador irá contar desde a primeira tentativa
computador = randint(0, 10)
jogador = int(input("Pensei em um número entre 0 e 10. Qual o seu palpite? "))

while jogador != computador: # o loop irá parar somente quando o número do jogador for igual ao número do computador
    cont += 1
    if jogador > computador:
        print("Menos... ")
    if jogador < computador:
        print("Mais... ")
    jogador = int(input("Faça um novo palpite: "))
print(f"Acertou! Foram necessárias {cont} rodadas. Parabéns!")
