"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

ano = int(input('Informe um ano: '))

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'\nO ano de {ano} é um ano Bissexto!')
else:
    print(f'\nO ano de {ano} não é um ano Bissexto!')
