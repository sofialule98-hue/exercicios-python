# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper().strip()

print(f"A letra 'A' aparece {frase.count('A')} vezes. \n"
      f"Primeira Posição: {frase.find('A') + 1} \n"
      f"Última Posição: {frase.rfind('A') + 1} ") # o uso do r no find é para que a leitura comece do lado direito
