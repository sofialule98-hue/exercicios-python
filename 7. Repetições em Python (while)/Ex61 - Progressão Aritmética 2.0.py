# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("+" * 25)
print("PROGRESSÃO ARITMÉTICA 2.0")
print("+" * 25)
print()

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
cont = 1
while cont <= 10: # enquanto o contador for menor ou igual a 10 será feito a soma do termo com a razão para determinar a PA
     print(f"{termo} -> ", end='') # o resultado das 10 somas irá aparecer na tela separadas por uma seta
     termo += razao
     cont += 1

print("FIM")
