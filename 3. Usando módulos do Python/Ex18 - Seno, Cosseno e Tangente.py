# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
from math import radians

a = float(input("Digite um ângulo: "))

print(f"O ângulo {a:.0f} possui seno {math.sin(radians(a)):.2f}, cosseno {math.cos(radians(a)):.2f} e tangente {math.tan(radians(a)):.2f}.") # realizei uma simplificação na
# quantidade de variáveis aplicando o cálculo diretamente no .format
