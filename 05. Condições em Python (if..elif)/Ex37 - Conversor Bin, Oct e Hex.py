# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um número inteiro: "))
conversao = int(input("Escolha uma das bases para conversão: \n"
                      "[ 1 ] converter para BINÁRIO \n"
                      "[ 2 ] converter para OCTAL \n"
                      "[ 3 ] converter para HEXADECIMAL \n"
                      "Sua opção: "))
if conversao == 1:
    numero_binario = bin(n)[2:] # o [2:] serve para remover o prefixo
    print(f"O número {n} em binário é igual a {numero_binario}")
elif conversao == 2:
    numero_octal = oct(n)[2:]
    print(f"O número {n} em octal é igual a {numero_octal}")
elif conversao == 3:
    numero_hexa = hex(n)[2:]
    print(f"O número {n} em hexadecimal é igual a {numero_hexa}")
else:
    print("Opção inválida. Tente novamente.")
