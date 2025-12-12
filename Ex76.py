# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Nota: Decidi a partir deste exercício utilizar as aspas de forma mais consciente. Irei usar aspas simples para strings simples ' ' e
# aspas duplas para string compostas "' '".

print('=' * 26)
print(f'{"- LISTAGEM DE PREÇOS -":^26}') # para centralizar a string é possível formatar com :^ e o tamanho desejado
print('=' * 26)

produtos = ('Queijo', 8, 'Salame', 15, 'Pão', 1.99, 'Requeijão', 6 , 'Alface', 4.99)
for i in range(len(produtos)):
    if i % 2 == 0: # Posição par = nome do produto
        print(f'{produtos[i]:.<19}', end='') # Alinha à esquerda, preenche com pontos
    else: # Posição ímpar = preço
        print(f'R${produtos[i]:>5.2f}') # Alinha à direita, 2 casas decimais

print('\nCompre todos esses itens para montar um sanduiche delicioso! :)')