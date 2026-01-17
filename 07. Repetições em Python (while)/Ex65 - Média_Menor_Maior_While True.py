# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

soma = maior = menor = 0
resp = ''
cont = 1
numero = int(input("Digite um número: "))
while True:
    if cont == 1:
        maior = menor = numero
    if numero > maior:
        maior = numero
    else:
        menor = numero
    soma += numero
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if resp == 'N':
        break
    else:
        numero = int(input("Digite um número: "))
    cont += 1
media = soma / cont
print(f"A média dos {cont} valores lidos é igual a {media}\n"
      f"O maior número lido foi {maior} e o menor foi {menor}.")
