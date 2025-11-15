# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
from math import trunc

real = float(input("Digite um número real: "))

print(f"O número digitado foi {real}. A porção inteira deste número é {trunc(real)}.")
