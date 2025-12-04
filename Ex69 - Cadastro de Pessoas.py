# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulheres = 0
quant = 0

print('=== CADASTRO DEMOGRÁFICO ===\n')

while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in ('F', 'M'):
        entrada = str(input("Digite seu sexo [F/M]: ")).strip().upper()
        if sexo and entrada[0] in 'FM':
            sexo = entrada[0]
        else:
            print("Por favor, digite F ou M.")
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    quant += 1
    continuar = ' '
    while continuar not in ('S', 'N'):
        entrada = str(input("Deseja continuar [S/N]? ")).strip().upper()
        if continuar and entrada[0] in 'SN':
            continuar = entrada[0]
        else:
            print("Por favor, digite S ou N.")
    if continuar == 'N':
        break

print("\n" + "=" * 35)
print("RESULTADOS DO CADASTRO:")
print("=" * 35)
print(f"Total de pessoas cadastradas: {quant}")
print(f"Pessoas com mais de 18 anos: {maiores}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheres}")
print("=" * 35)
