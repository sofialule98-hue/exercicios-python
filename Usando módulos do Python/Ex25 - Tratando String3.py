# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo: ")).upper().strip()

print(f"Tem Silva no nome? {'SILVA' in nome}") # o operador de pertinência 'in' irá verificar se na string existe 'Silva' independende da posição e irá retornar True ou False
