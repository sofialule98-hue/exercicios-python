# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1 # para que seja possível realizar a múltiplicação a variável fatorial precisa iniciar com 1
contador = numero # o contador é igual ao número porque com o while o cálculo é feito como uma contagem regressiva, do maior para o menor

print("-" * 15)
print(f"Calculando {numero}!: ", end='')
while contador > 0: # quando o contador chegar em 0, a repetição é interrompida e segue para o print(fatorial)
    fatorial *= contador # o cálculo do fatorial inicia... variável fatorial  = 1 * o número informado (ex: 5), então: 1 * 5 = 5... a variável fatorial irá receber o valor 5
    print(contador, end='')
    print(" x " if contador > 1 else ' = ', end='')
    contador -= 1 # para que o cálculo seja feito, a cada loop é subtraído 1 do valor da variável contador,
    # então a cada loop a multiplicação será 1 * 5 = 5 / 5 * 4 = 20 / 20 * 3 = 60 / 60 * 2 = 120 / 120 * 1 = 120 (contador chega no 0 e para)
print(fatorial)
