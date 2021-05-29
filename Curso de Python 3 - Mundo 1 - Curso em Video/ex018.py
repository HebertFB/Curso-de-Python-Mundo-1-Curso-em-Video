"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo"""

import math
num = float(input('Informe um ângulo: '))

print(f'O ângulo informado é {num} e seu seno é {math.sin(math.radians(num)):.2f}'
      f'\nO cosseno é {math.cos(math.radians(num)):.2f}'
      f'\nE a sua tangente é {math.tan(math.radians(num)):.2f}')
