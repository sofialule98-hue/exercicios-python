# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

a = input("Digite seu nome: ")
b = input("Digite seu nome: ")
c = input("Digite seu nome: ")
d = input("Digite seu nome: ")

lista = [a, b, c, d]
escolhido = random.choice(lista)

print(f"O aluno sorteado foi {escolhido}.")
