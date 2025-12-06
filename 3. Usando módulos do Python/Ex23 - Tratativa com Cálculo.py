#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input("Digite um número de 0 a 9999: "))

unidade = numero // 1 % 10 # cálculo onde primeiro é feito a divisão onde retorna somente o número inteiro e por fim verifica qual o módulo (o resto) da divisão por 10  
dezena = numero // 10 % 10 # a primeira divisão é feita e muda de acordo com a classe do número que será exibido na tela 
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Analisando o número {numero}\n"
      f"Unidade: {unidade}\n"
      f"Dezena: {dezena}\n"
      f"Centena: {centena}\n"
      f"Milhar: {milhar}\n")

