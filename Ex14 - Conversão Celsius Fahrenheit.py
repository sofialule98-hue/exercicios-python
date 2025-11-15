# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = int(input("Digite a temperatura em Celsius: "))
f = (c * 1.8) + 32

print(f"A temperatura convertida em Fahrenheit é {f:.0f} °F.")
