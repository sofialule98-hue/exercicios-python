# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))

while True: # o valor booleano True fará com que o programa funcione infinitamente até que o usuário selecione a opção 5 - sair do programa
    sleep(0.55)
    menu = int(input("MENU DE OPÇÕES: \n"
                     "[ 1 ] Somar \n"
                     "[ 2 ] Multiplicar \n"
                     "[ 3 ] Maior \n"
                     "[ 4 ] Novos Números \n"
                     "[ 5 ] Sair do Programa \n"
                     "Digite o número da operação desejada: "))
    if menu == 1:
        soma = n1 + n2
        print(f"A soma dos números {n1} e {n2} é igual a {soma}.")
    elif menu == 2:
        mult = n1 * n2
        print(f"A multiplicação entre os números {n1} e {n2} é igual a {mult}.")
    elif menu == 3:
        if n1 > n2:
            print(f"O número {n1} é maior que {n2}.")
        elif n1 < n2:
            print(f"O número {n2} é maior que {n1}.")
        else:
            print(f"Os números {n1} e {n2} são iguais!")
    elif menu == 4:
        print("Limpando os números antigos...")
        n1 = int(input("Digite o 1º valor? "))
        n2 = int(input("Digite o 2º valor? "))
    elif menu == 5:
        print("Obrigado por usar este programa!")
        break # sai do loop imediatamente e exibe a mensagem de encerramento do programa
    else:
        print("Opção inválida! Tente novamente.")
        sleep(1) # espera 1 segundo para continuar o loop
print()
print("Programa encerrado.")

