from time import sleep, strftime, localtime
from datetime import datetime
"""Mostar o horario exato dentro de uma atualização do for"""

for numero in range(5):
    sleep(1)
    datahora = datetime.now()
    print(f'Esse é o DateHora: {datahora}\n')

    t = localtime()
    agora = strftime("%H:%M:%S / %d/%m/%y", t)
    print(f'Esse é o agora: {agora}\n')

    now = datetime.now().time()
    print(f'Esse é o now: {now}\n')

