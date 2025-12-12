# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('Python', 'Programar', 'Criar', 'Analisar', 'Inovar', 'Aprender', 'Tecnologia', 'Pratica', 'Futuro')

for p in palavras: # o for repete cada índice da tupla
    print(f'\nA palavra {p.upper()} tem', end=' ')
    for letra in p: # o for verifica cada elemento (letra) de cada índice (palavra)
        if letra.lower() in 'aeiou': # o lower é utilizado nesta condição para conseguir contabilizar as letras em maiúsculo
            print(letra.lower(), end=' ') # todas as vogais aparecem em letra minúscula
