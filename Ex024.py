# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome da cidade: ").upper().strip()

print(f"Começa com Santo? {cidade[:5] == 'SANTO'}")

