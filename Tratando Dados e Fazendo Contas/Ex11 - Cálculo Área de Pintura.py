# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Digite a largura da parede em metros: "))
a = float(input("Digite a altura da parede em metros: "))

area = l * a
tinta = area / 2

print(f"Para pintar uma parede com área de {area} m² será necessário {tinta} L de tinta.")
