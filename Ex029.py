# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7 # a resolução consiste em subtrair o valor onde a velocidade é permitida para multiplicar o resto pelo valor da multa
    print(f"Você ultrapassou a velocidade permitida! Sua multa custará R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade! Continue assim.")
