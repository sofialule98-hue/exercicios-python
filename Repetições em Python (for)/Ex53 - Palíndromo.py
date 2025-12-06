# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase qualquer: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f"Você digitou a frase {junto}")

for letra in range(len(junto) - 1, -1, -1): # letra é o índice, então irá ler de letra em letra. o range será contado o tamanho da string digitada pelo usuário sem
    # os espaços internos com -1 para não ler o caracter invisível, até -1 para que seja lido toda a frase e novamente o -1 para que seja lido de trás para frente
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
