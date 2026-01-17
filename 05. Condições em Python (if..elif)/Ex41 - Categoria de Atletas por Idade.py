#  Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
#  um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

nascimento = int(input("Digite seu ano de nascimento: "))

idade = date.today().year - nascimento

if idade <= 9:
    print(f"Você tem {idade} anos. Sua categoria é a MIRIM.")
elif idade <= 14:
    print(f"Você tem {idade} anos. Sua categoria é a INFANTIL.")
elif idade <= 19:
    print(f"Você tem {idade} anos. Sua categoria é a JÚNIOR.")
elif idade <= 25:
    print(f"Você tem {idade} anos. Sua categoria é a SÊNIOR.")
else:
    print(f"Você tem {idade} anos. Sua categoria é a MASTER.")
