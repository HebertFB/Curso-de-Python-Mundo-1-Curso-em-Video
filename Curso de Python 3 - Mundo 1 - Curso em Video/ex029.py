"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite"""

km = float(input('Quantos Km/h o carro está? '))

if km > 80:
    print(f'\nVocê está acima da velocidade permitida de 80Km/h!'
          f' E foi multado em R$ {(km - 80) * 7:.2f}!')
else:
    print('\nBom dia! Dirija com segurança!')
