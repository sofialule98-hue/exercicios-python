# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper().strip()

print(f"A letra 'A' aparece {frase.count('A')} vezes. \n" # a função count irá contar quantas vezes a letra 'A' aparece
      f"Primeira Posição: {frase.find('A') + 1} \n" # a função find irá fazer uma varredura da esquerda para a direita para localizar a primeira posição de 'A', o + 1 existe pois a contagem inicia no zero, e se a letra 'A'
      # estiver nesta primeira posição, o programa irá retornar 0 e não 1 como o usuário espera
      f"Última Posição: {frase.rfind('A') + 1} ") # o uso do r no find é para que a leitura comece do lado direito

