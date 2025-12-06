# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b > c:
    print(f"O número {a} é o maior valor.")
elif b > a > c:
    print(f"O número {b} é o maior valor.")
else:
    print(f"O número {c} é o maior valor.")

if a < b < c:
    print(f"O número {a} é o menor valor.")
elif b < a < c:
    print(f"O número {b} é o menor valor.")
else:
    print(f"O número {c} é o menor valor.")
