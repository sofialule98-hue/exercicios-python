# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input("Digite seu nome completo: ")).title().strip().split() # adicionei a função title para que na saída dos dados os nomes apareçam com a primeira letra maiúscula e split para inserir cada nome em uma lista
print(f"Seu primeiro nome é {nome[0]}, e o último é {nome[- 1]}.") # ou nome[len(nome) - 1] pois o len irá contar cada nome que foi separado pelo split, as listas
# começam sempre com 0, então o -1 é a forma de conseguir mostrar o último objeto da lista, se for -2 irá mostrar a penúltima e assim por dia ou simplesmente colocar [-1] pois desta
# forma ele automaticamente puxa o último objeto de forma simplificada.

