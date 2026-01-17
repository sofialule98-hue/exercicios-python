# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

analise = []
expressao = input('Digite uma expressão matemática: ').strip()
for simbolo in expressao:
    if simbolo == '(':
        analise.append('(')
    elif simbolo == ')':
        if len(analise) > 0:
            analise.pop()
        else:
            analise.append(')')
            break
if len(analise) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
