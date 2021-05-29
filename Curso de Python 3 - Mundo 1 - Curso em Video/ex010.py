"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar"""

reais = float(input('Informe quantos Reais a ser convertido para Dólar: '))
cotacao = float(input('Informe a cotação atual do Dólar: '))

print(f'R${reais:.2f} Reais convertidos dará US${reais/cotacao:.2f} Dólares!')
