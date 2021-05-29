"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR"""

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'\nO número {num} é par!')
else:
    print(f'\nO número {num} é ímpar!')
