# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
while True: # Loop infinito para coletar múltiplos números
    valor = int(input('Digite um número: '))
    lista.append(valor) # Adiciona o valor à lista
    cont += 1 # Incrementa o contador
    resp = input('Deseja continuar [S/N]? ').strip().upper()
    if resp not in 'SN':
        resp = input('Por favor, digite S para sim e N para não. Deseja continuar [S/N]? ').strip().upper()
    if resp == 'N':
        break
lista.sort(reverse=True) # Ordena os valores da lista em ordem decrescente
print('=' * 21)
print(f'{"- VALORES COLETADOS -":^15}')
print('=' * 21)
print(f'Total de números digitados: {cont}')
print('Lista de valores em ordem decrescente: ', end='')
# Exibe a lista formatada (sem vírgula final)
for i in lista:
    print(f'{i}', end=', ' if i != lista[-1] else '') # Se não for o último elemento, adiciona vírgula e espaço
    # Se for o último, apenas o número (sem vírgula)
# Se tiver 5 na lista
if 5 in lista:
    print('\nO valor 5 FOI digitado! Está na posição: ', end='')
    posicoes = [] #lista para identificar a posição do número 5
    for i, numero in enumerate(lista): # enumerate() retorna pares (índice, valor) para cada elemento
        if numero == 5:
            posicoes.append(i + 1) # Adiciona a posição (índice + 1 porque listas começam em 0)
    for pos in posicoes: # Exibe todas as posições encontradas
        print(f'{pos}ª', end=', ' if pos != posicoes[-1] else '')  # Formatação parecida: vírgula apenas entre posições, não no final
else:
    print("\nO valor 5 não foi digitado e não está na lista.")
