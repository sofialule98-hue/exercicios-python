# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))

h = math.hypot(oposto, adjacente)

print(f"O comprimento da hipotenusa é {h:.2f}")
