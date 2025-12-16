# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Este número já existe e não será adicionado! ')
    else:
        lista.append(valor)
    resp = input('Deseja continuar [S/N]? ').strip().upper()
    while resp not in 'SN':
        resp = input('Por favor, digite S para sim ou N para não. Deseja continuar [S/N]? ').strip().upper()
    if resp == 'N':
        break
lista.sort()
print(f'Os valores digitados foram: ', end='')
for i in lista:
    print(f'{i}', end=' ')
