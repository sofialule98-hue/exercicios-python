# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1: # esta condição permite que as variáveis maior e menor sejam atribuídas ao primeiro valor lido, desta forma, é possível fazer um comparativo com os próximos valores para determinar
        # qual é o maior e o menor.
        maior = peso
        menor = peso
    else:
        if peso > maior: # verifica qual o maior peso
            maior = peso
        if peso < menor: # verifica qual o menor peso
            menor = peso
print(f"A pessoa com maior peso tem {maior:.1f}Kg e a pessoa com menor peso tem {menor:.1f}Kg.")

