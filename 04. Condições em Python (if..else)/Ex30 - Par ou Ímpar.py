# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0: # a condição verifica se o resto do número informado divido por 2  é igual a zero, determinando assim se o número é par ou ímpar
    print(f"O número que você digitou foi {numero}, ele é PAR!")
else:
    print(f"O número que você digitou foi {numero}, ele é IMPAR!")

