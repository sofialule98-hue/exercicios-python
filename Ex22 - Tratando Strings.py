# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip()

print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Seu nome possui ao todo {len(nome) - nome.count(' ')} letras.") # ao contar quantos caracteres possui uma string e contar quantos espaços é possível realizar uma subtração para verificar quantos caracteres possui
# um objeto específico

separa = nome.split()
print(f"Seu primeiro nome é {separa[0].capitalize()} e possui {len(separa[0])} letras.")

