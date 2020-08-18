from openpyxl import load_workbook
from random import choice
"""Importar a base do Excel e Randomizar a escolha das celulas"""
wb = load_workbook('coisas.xlsx')
plan = wb['Planilha1']
lista = plan['A']
print(len(lista))

for click in range(300):
    arroba = choice(lista)
    print(f'{click + 1} - Voce Marcou: {arroba.value}')

input("DIGITE ALGO PARA SAIR")