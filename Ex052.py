# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
cont = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[33m", end='')
        cont += 1
    else:
        print("\033[31m", end='')
    print(f"{i} ", end='')
print(f"\n\033[mO número {numero} foi divisível {cont} vezes", end=' ')
if cont == 2:
    print("e por isso ele É PRIMO!")
else:
    print("e por isso ele NÃO É PRIMO!")