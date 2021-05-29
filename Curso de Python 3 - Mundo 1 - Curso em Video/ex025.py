"""Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome"""

nome = input('Digite um nome: ').strip()

print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
