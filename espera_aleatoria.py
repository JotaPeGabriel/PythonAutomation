from openpyxl import load_workbook
from time import sleep, localtime, strftime
from random import choice

"""Importar a base do Excel, Randomizar a escolha das celulas e tempo"""

folha = load_workbook('database_test.xlsx')
plan = folha['dados']
lista = plan['A']
plant = folha['tempo']
listat = plant['A']
print(f'Aqui tem {len(lista)} Linhas')
print(f'Aqui tem {len(listat)} Linhas')

for click in range(len(lista)):
    arroba = choice(lista)  # escolhe um Arroba aleatorio da coluna A

    t = localtime()  # localiza o tempo atual
    agora = strftime("%H:%M:%S", t)  # Seta o tempo nos padroes

    print(f'{click + 1} - Esse é o escolhido >> {arroba.value} em {agora}<<')

    tempo = choice(listat)   # escolhe um tempo aletorio
    print(f'O proximo vai ser daqui a >> {tempo.value} Segs ou aproximadamente {int(tempo.value)/60:.2f} Minutos <<\n')
    sleep(tempo.value)
