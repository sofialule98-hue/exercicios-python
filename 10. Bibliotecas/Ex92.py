# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - dados['Nascimento']
dados['CTPS'] = int(input('Número CTPS (Didite 0 caso não possua): '))
if dados['CTPS'] != 0:
    dados['Ano_de_Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Ano_de_Aposentadoria'] = dados['Ano_de_Contratação'] + 35
    dados['Idade_Aposentadoria'] = dados['Idade'] + 35
print('=' * 30)
print("DADOS CADASTRADOS".center(30))
print('=' * 30)
for chave, valor in dados.items():
    chave_formatada = chave.replace('_', ' ').title()
    if chave == 'Salário':
        print(f'{chave_formatada}: R${valor:.2f}')
    else:
        print(f'{chave_formatada}: {valor}')
if dados['CTPS'] != 0:
    print('-' * 40)
    print(f'{dados["Nome"]} irá se aposentar com {dados["Idade_Aposentadoria"]} anos em {dados["Ano_de_Aposentadoria"]}.')

