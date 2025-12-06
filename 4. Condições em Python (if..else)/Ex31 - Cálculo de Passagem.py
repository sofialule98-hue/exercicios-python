# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
# de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f"Sua viagem será de {distancia}Km, sua passagem irá custar R${passagem:.2f}")
