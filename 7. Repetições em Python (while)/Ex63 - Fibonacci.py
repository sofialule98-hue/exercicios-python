# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
#
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print("-" * 23)
print("Sequência de Fibonacci")
print("-" * 23)
termos = int(input("Digite a quantidade de termos: "))
t1 = 0 # na sequência os dois primeiros termos precisam ser 0 e 1
t2 = 1
cont = 3 # dessa forma o contador começa do terceiro termo em diante
print(f"{t1} -> {t2}", end='')
while cont <= termos: # para o loop continuar o contador precisa ser
    # menor igual ao número de termos solicitados pelo usuário
    t3 = t1 + t2 # soma que resulta no terceiro termo
    print(f" -> {t3}", end='')
    t1 = t2 # para que o programa consiga somar o número de termos solicitados, é realizado
    # uma substituição de valores nas variáveis que realizam a soma
    t2 = t3 # então enquanto o loop estiver ativo, ele consegue fazer a soma
    # dos dois últimos números até que finalize a quantidade de termos da forma correta
    cont += 1
