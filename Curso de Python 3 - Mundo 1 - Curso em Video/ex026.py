"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez"""

frase = input('Digite algo: ').strip().upper()

print(f'\nA letras A aparece {frase.count("A")} vezes')
print(f'´A´ aparece a primeira vez na posição {frase.find("A")+1}')
print(f'´A´ aparece a última vez na posição {frase.rfind("A")+1}')
