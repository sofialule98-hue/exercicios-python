# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - nascimento # cálculo necessário para descobrir a idade atual do usuário

if idade == 18:
    print(f"Você tem {idade} anos. Se aliste ao serviço militar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Você tem {idade} anos. Faltam {saldo} anos para você poder se alistar ao serviço militar!")
    ano = date.today().year + saldo
    print(f"Seu alistamento será em {ano}.")
elif idade <= 45:
    saldo = idade - 18
    print(f"Você tem {idade} anos. Deveria ter se alistado há {saldo} anos!")
    ano = date.today().year - saldo
    print(f"Seu alistamento foi em {ano}.")
else:
    print(f"Você tem {idade} anos. O prazo para se alistar já passou.")

