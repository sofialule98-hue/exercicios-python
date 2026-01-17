# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("+" * 22)
print("PROGRESSÃO ARITMÉTICA")
print("+" * 22)
print(" ")

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao # o enunciado pede os 10 primeiros números, porém na estrutura de repetição se eu colocar (primeiro, 10, razao), o programa vai contar até o número 10.
# se o primeiro termo for maior que 10, a progressão não irá aparecer na tela. então a variável decimo é o cálculo da enésima posição que será somada com o primeiro termo, tendo assim 10 termos.

for i in range(primeiro, decimo + 1, razao):
    print(f"{i}", end=' -> ')
print("FIM")
