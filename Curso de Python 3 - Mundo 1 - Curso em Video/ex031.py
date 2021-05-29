"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas"""

km = float(input('Informe a distância da viagem em Km: '))

if km > 200:
    print(f'\nO preço da passagem para viajar {km}Km será de R${km * 0.45:.2f}')
else:
    print(f'\nO preço da passagem para viajar {km}Km será de R${km * 0.50:.2f}')
