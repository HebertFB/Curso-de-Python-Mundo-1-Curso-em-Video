"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras tem o nome completo sem considerar espaços.
– Quantas letras tem o primeiro nome."""

nome = input('Digite seu nome completo: ')

print(f'\nMAIÚSCULO: {nome.upper()}')
print(f'minúsculo: {nome.lower()}')
separado = nome.split()
print(f"O nome completo tem {len(''.join(separado))} letras.")
print(f'O primeiro nome tem {len(separado[0])} letras.')
