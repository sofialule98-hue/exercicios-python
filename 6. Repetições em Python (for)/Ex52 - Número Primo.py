# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
cont = 0

for i in range(1, numero + 1):
    if numero % i == 0: # este condicional irá verificar se a divisão do número pelo contador i é igual a zero 
        print("\033[33m", end='') # adição de cor amarela à string
        cont += 1
    else:
        print("\033[31m", end='') # adição de cor vermelha à string
    print(f"{i} ", end='') # o programa irá mostrar na tela cada loop de número verificado, os divisíveis por 1 e por si mesmo ficam amarelo e o resto fica vermelho
print(f"\n\033[mO número {numero} foi divisível {cont} vezes", end=' ')
if cont == 2: # este condicional impõe que somente o total de 2 divisões configuram o número informado como primo. 
    print("e por isso ele É PRIMO!")
else:

    print("e por isso ele NÃO É PRIMO!")
