"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros"""

metros = float(input('Informe quantos metros a ser convertido: '))

print(f'\n{metros}m convertidos são {metros*100:.0f}cm'
      f'\nE {metros}m convertidos são {metros*1000:.0f}mm')
