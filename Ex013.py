# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu atual salário: "))

novo_salario = salario + (salario * 0.15)

print(f"Com aumento de 15%, seu salário subiu para {novo_salario} reais.")
