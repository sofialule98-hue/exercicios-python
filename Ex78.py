# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
# maior e o menor valor digitado e as suas respectivas posições na lista.

maior = menor = None
valores = list() # criado uma lista vazia
for i in range(5):
    valores.append(int(input(f'Digite o {i + 1}º valor: '))) # o for irá ler 5 inputs e adicionar à lista
    if i == 0: # se o primeiro índice receber o primeiro valor, este valor será tribuído às variáveis maior e menor
        # desta forma é possível realizar o comparativo
        maior = valores[i] # como estou lidando com uma lista, agora é necessário evidenciar que se trata do índice da lista
        menor = valores[i] # se eu colocar apenas 'valores', será interpretado como toda a lista e dará erro.
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print(f'Você digitou os valores {valores}')
print(f'O maior valor inserido foi {maior}', end='')
for i, v in enumerate(valores): # para determinarmos o índice do valor desejado
    if v == maior: # se o valor for igual ao valor na variável maior
        print(f' na posição {i + 1}.') # irá aparecer na tela a posição deste maior valor
print(f'O menor valor inserido foi {menor}', end='')
for i, v in enumerate(valores):
    if v == menor: # o mesmo método pode ser utilizado para determinar a posição do menor valor
        print(f' na posição {i + 1}.')