# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

print("-" * 22)
print("Calculadora de Tabuada")
print("-" * 22)

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        print("Número negativo!")
        break
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")
    print('-' * 13)

print("Fim do programa.")
