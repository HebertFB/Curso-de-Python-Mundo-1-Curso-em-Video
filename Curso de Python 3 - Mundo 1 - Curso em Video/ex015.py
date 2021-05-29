"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado"""

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados pelo carro? '))

print(f'\nA diaria de aluguel do carro é de R$60,00. {dias} dias = R${dias*60:.2f}'
      f'\nA rodagem é de R$0,15 por Km. {km}Km = R${km*0.15:.2f}'
      f'\nO total a ser pago será de R${(dias*60)+(km*0.15):.2f}!')
