# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
par = []
impar = []
while True:
    valor = int(input('Digite um número: '))
    numeros.append(valor)
    if valor % 2 == 0:
        par.append(valor)
        par.sort()
    else:
        impar.append(valor)
        impar.sort()
    resp = input('Deseja continuar [S/N]? ').strip().upper()
    while resp not in 'SN':
        resp = input('Por favor, digite S para sim e N para não. Deseja continuar [S/N]? ').strip().upper()
    if resp == 'N':
        break
print('=' * 20)
print(f'{"ANÁLISE DOS VALORES":^20}')
print('=' * 20)
numeros.sort()
print('VALORES COLETADOS: ', end='')
for i in numeros:
    print(f'{i}', end=', ' if i != numeros[-1] else '')
print('\nVALORES PAR: ', end='')
for i in par:
    print(f'{i}', end=', ' if i != par[-1] else '')
print('\nVALORES ÍMPAR: ', end='')
for i in impar:
    print(f'{i}', end=', ' if i != impar[-1] else '')
