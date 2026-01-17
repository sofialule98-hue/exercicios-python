# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

media = (n1 + n2) / 2

print(f"A média das notas {n1:.1f} e {n2:.1f} é igual a {media:.1f}!")
