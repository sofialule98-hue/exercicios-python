# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

nomevelho = ''
maioridadehomem = 0
cont = 0
soma = 0
for i in range(1, 5):
    print(f"---- {i}ª Pessoa ----")
    nome = str(input("Nome: ")).strip() # retirado os espaços externos
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip() # retirado os espaços externos
    if sexo in 'Ff' and idade < 20: # condicional para contagem de idade inferior à 20 anos de mulheres
        cont += 1
    if i == 1 and sexo in 'Mm': # a partir do primeiro índice se for homem irá armazenar nas variáveis sua idade e nome
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: # condicional para averiguar homem mais velho
        maioridadehomem = idade
        nomevelho = nome
    soma += idade
    media = soma / 4 # cálculo de média
print(f"A média de idade do grupo é de {media} anos.")
print(f"O grupo possui {cont} mulheres com menos de 20 anos.")
print(f"O homem mais velho do grupo tem {maioridadehomem} anos e se chama {nomevelho}.")
