# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = [] # Lista vazia para armazenar valores
for i in range(5): # Loop para coletar 5 valores
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if i == 0 or valor > lista[-1]: # Primeiro valor OU maior que todos existentes
        lista.append(valor) # Adiciona ao final da lista
    else: # Senão, o valor precisa ser inserido em posição específica
        pos = 0 # # Começa verificando desde o início da lista
        while pos < len(lista): # Percorre a lista até encontrar onde o valor deve ficar
            if valor <= lista[pos]: # Se valor for menor ou igual ao valor na posição atual
                lista.insert(pos, valor) # Se sim, insere na posição encontrada, jogando o valor antigo para a posição seguinte
                break # Sai do loop - valor já foi inserido
            pos += 1 # Avança para próxima posição se não encontrou
print('=' * 40)
print(f'Os valores digitados em ordem foram: ', end='')
for i in lista: # Exibe a lista ordenada
    print(i, end=' ')
