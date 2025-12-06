# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade

peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))

imc = peso / (altura ** 2)

if imc > 30:
    print(f"Seu IMC está em {imc:.1f}, você está com OBESIDADE. Procure um médico imediatamente.")
elif (imc <= 30) and (imc >= 25):
    print(f"Seu IMC está em {imc:.1f}, você está com SOBREPESO. Cuide-se.")
elif (imc < 25) and (imc >= 18.5):
    print(f"Seu IMC está em {imc:.1f}, você está com PESO IDEAL. Parabéns!")
else:
    print(f"Seu IMC está em {imc:.1f}, você está ABAIXO DO PESO. Procure um médico imediatamente.")
