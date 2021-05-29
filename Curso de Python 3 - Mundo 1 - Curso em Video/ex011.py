"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de
2 metros quadrados"""

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

print(f'\nA área da parede é de {largura*altura}m²!!')
print(f'Será necessário {(largura*altura)/2} litros de tinta para pinta a parede!')
