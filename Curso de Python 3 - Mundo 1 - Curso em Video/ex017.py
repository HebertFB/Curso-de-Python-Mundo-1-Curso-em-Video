"""Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa"""

from math import hypot
ca = float(input("Informe o cateto adjacente: "))
co = float(input('Informe o cateto oposto: '))

print(f'A hipotenusa do triângulo retângulo é {hypot(ca,co):.2f}')
