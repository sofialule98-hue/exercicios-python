# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year # este método de classe date.today() retorna a data de hoje e o year retorna um valor armazenado no objeto, é um atributo que retorna espeficicamente o ano
    # sem o dia e o mês que estão presentes no today()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # as condições necessárias para que o ano seja bissexto consistem em: o resto da divisão do ano por 4 precisa ser igual a 0.
    # para tratar excessões o resto da divisão por 100 precisa ser diferente de 0 para não englobar anos como 1700 ou 1900 que são divisíveis por 4 ou o resto da
    # divisão por 400 precisa ser igual a 0.
    print(f"O ano {ano} é BISSEXTO!")
else:
    print(f"O ano {ano} NÃO é BISSEXTO!")
