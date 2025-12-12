#  Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {tupla[numero]}.")
    else:
        print("Número fora do intervalo!", end=' ')
        continue
    continuar = input("Deseja continuar [S/N]? ").strip().upper()
    while continuar not in 'SN':
        continuar = input("Por favor digite S para sim e N para não. Deseja continuar [S/N]? ").strip().upper()
    if continuar == "N":
        break
print("Fim do programa!")
