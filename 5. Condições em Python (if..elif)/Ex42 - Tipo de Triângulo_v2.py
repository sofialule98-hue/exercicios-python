# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))

if r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2: # para uma forma geométrica ser um triângulo a soma de duas retas precisa ser maior ou igual
    # à terceira reta
    print(f"Os valores {r1:.1f}, {r2:.1f} e {r3:.1f} podem formar um triângulo ", end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print(f"Os valores {r1:.1f}, {r2:.1f} e {r3:.1f} NÃO podem formar um triângulo!")
