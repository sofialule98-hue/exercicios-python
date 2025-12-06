# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

br = float(input("Quanto de dinheiro você tem na carteira? "))

dol = br / 5.30 # cotação do dólar em 11/2025

print(f"Você consegue comprar {dol:.2f} dólares com {br} reais.")
