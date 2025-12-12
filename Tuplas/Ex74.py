# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint
aleatorio = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))

print("5 Números Aleatórios (0, 50):")
for i in aleatorio: # a iteração no for irá puxar cada índice dos 5 números sorteados
    print(f"{i}", end=' ')
print(f"\nO maior valor sorteado foi {max(aleatorio)}.") # método para verificar e exibir qual o maior valor da tupla
print(f"O menor valor sorteado foi {min(aleatorio)}.") # método para verificar e exibir qual o menor valor da tupla
# estes métodos funcionam com qualquer iterável
