"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import randint

print('Tente advinha! Pensando em um número entre 0 a 5...')

pc = randint(0, 5)
player = int(input('\nQual número o computador pensou? '))
if pc == player:
    print(f'Você acertou! O número é {pc}')
else:
    print(f'Voçê errou! O número é {pc}')
