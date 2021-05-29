"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”"""

cidade = input('Informe o nome de uma cidade: ').strip()
print(f"{cidade[:5].upper() == 'SANTO'}")
