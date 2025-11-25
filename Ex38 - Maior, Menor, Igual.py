# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero_1 = int(input("Digite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))

if numero_1 > numero_2:
    print("O primeiro valor é maior.")
elif numero_2 > numero_1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
