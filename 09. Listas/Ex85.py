#  Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
valor = 0
for i in range(7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print('=' * 20)
print(f'{"VALORES COLETADOS:":^20}')
print('=' * 20)
print('Pares: ', end='')
if valores[0]:
    for i, num in enumerate(valores[0]):
        print(f'{num}', end= ', ' if i != len(valores[0])-1 else '.')
else:
    print('Nenhum número par digitado.', end='')
print('\nÍmpares: ', end='')
if valores[1]:
    for i, num in enumerate(valores[1]):
        print(f'{num}', end=', ' if i != len(valores[1])-1 else '.')
else:
    print('Nenhum número ímpar digitado.', end='')
