# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome da cidade: ").upper().strip() # os dados inseridos pelo usuário são convertidos em maiúsculo e se houver espaços, serão removidos

print(f"Começa com Santo? {cidade[:5] == 'SANTO'}") # o programa irá analisar os 5 primeiros caracteres e verificar se possuem 'SANTO', se sim irá retornar True, senão, False
