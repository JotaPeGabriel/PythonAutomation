from openpyxl import load_workbook
from random import choice
"""Importar a base do Excel e Randomizar a escolha das celulas"""
wb = load_workbook('database_test.xlsx')
plan = wb['dados']
lista = plan['A']
plant = wb['tempo']
listat = plant['A']
print(len(lista))
print(len(listat))

for click in range(len(lista)):
    dado = choice(lista)
    tempo = choice(listat)
    print(f'A palavra foi {dado.value} e o tempo {tempo.value} segundos')
