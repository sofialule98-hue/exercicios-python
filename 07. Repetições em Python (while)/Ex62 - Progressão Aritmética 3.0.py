# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerrará quando ele disser que quer
# mostrar 0 termos.

print("+" * 25)
print("PROGRESSÃO ARITMÉTICA 3.0")
print("+" * 25)
print()

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0: # enquanto o usuário não quiser ver mais termos e teclar 0, o loop irá continuar
    total += mais # esta somatória permite que de início a PA tenha 10 termos e em sequência irá somar a quantidade de termos solicitados
    while cont <= total: # enquanto a contagem for menor ou igual ao total, o programa irá continuar realizando a somatória de mais termos
         print(f"{termo} -> ", end='')
         termo += razao
         cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")

