# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna = 0
maior = None
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha, coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_coluna += matriz[linha][coluna]
        if linha == 1:
            if maior is None or matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
print('-' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-' * 20)
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma dos valores da 3ª Coluna: {soma_coluna}')
print(f'Maior valor da 2ª Linha: {maior}')