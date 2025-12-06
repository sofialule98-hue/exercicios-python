# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input("Digite o comprimento da primeira reta: "))
reta_2 = float(input("Digite o comprimento da segunda reta: "))
reta_3 = float(input("Digite o comprimento da terceira reta: "))

if reta_1 + reta_2 >= reta_3 and reta_2 + reta_3 >= reta_1 and reta_1 + reta_3 >= reta_2: # para uma forma geométrica ser um triângulo a soma de duas retas precisa ser maior ou igual
    # à terceira reta
    print(f"As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f} podem formar um triângulo!")
else:
    print(f"As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f} NÃO podem formar um triângulo!")
