# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Das 7 pessoas, {maior} são maiores de idade e {menor} ainda não atingiram a maioridade.")

