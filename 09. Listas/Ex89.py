# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1º Semestre: '))
    nota2 = float(input('Nota 2º Semestre: '))
    media = (nota1 + nota2) / 2
    aluno = (nome, nota1, nota2, media) # um ótimo exemplo para se usar tupla, onde os dados são imutáveis.
    boletim.append(aluno) # tupla inserida em lista
    continuar = input('Para adicionar um novo aluno digite "+" \n'
                      'Para encerrar o programa digite "SAIR" \n'
                      '= ').strip().upper()
    while continuar not in ('+', 'SAIR'):
        continuar = input('Para adicionar um novo aluno digite "+" \n'
                          'Para encerrar o programa digite "SAIR" \n'
                          '= ').strip().upper()
    if continuar == 'SAIR':
        break
print('=' * 35)
print(f'{"BOLETIM":^35}')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 35)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[3]:>8.1f}', end=' - ')
    if aluno[3] <= 5.9:
        print('RECUPERAÇÃO!')
    else:
        print('APROVADO!')
while True:
    print('-' * 45)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FIM DO PROGRAMA.')
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]:.1f} e {boletim[opcao][2]:.1f}')
    else:
        print(f'Aluno não encontrado! Digite um número entre 0 e {len(boletim) - 1}')