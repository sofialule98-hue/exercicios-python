# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = []
pares = []
for i in range(4):
    lista.append(int(input(f"Digite o {i + 1}º valor: ")))
tupla = tuple(lista)
print("=" * 30)
print("Valores digitados: ", end='')
for i in tupla:
    print(f"{i}", end=' ')
print(f"\nQuantas vezes apareceu o valor 9: {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"Em que posição foi digitado o primeiro valor 3: {tupla.index(3) + 1}ª Posição.")
else:
    print("O número 3 não foi digitado em nenhuma posição.")
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
print("Números pares: ", end='')
if pares:
    for num in pares:
        print(f"{num}", end=' ')
else:
    print("0", end='')
