# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).
import sys

n = int(input("Digite um número (999 caso queira parar): "))
if n == 999:
    print("Saindo do programa!")
    sys.exit()
soma = 0
cont = 1
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número (999 caso queira parar): "))
    if n == 999:
        cont -= 1
print(f"Você digitou {cont} número, a soma entre eles é igual a {soma}.")
