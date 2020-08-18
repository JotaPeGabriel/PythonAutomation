from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep, localtime, strftime
from openpyxl import load_workbook
from random import choice

""" Projeto de automação - Python + Selenium + OpenPyXL """

url = 'https://www.instagram.com/p/CCqqjE0HxWb/'
navegador = Chrome()  # Define o Navegador como variavel
navegador.get(url)

folha = load_workbook('arrobas.xlsx')
plan = folha['Plan1']
lista = plan['A']
print('ANTES DE COMEÇAR ESTEJA LOGADO E NA TELA DO SORTEIO')
start = input("Quando estiver pronto digite algo: ")

balao = navegador.find_element_by_class_name('_15y0l')  # Encontrar e Clicar no Balao,Passando a vareavel arroba
marcar = balao.find_element_by_class_name('wpO6b')

classe = navegador.find_element_by_class_name('RxpZH')  # Encontrar e Clicar no botão ENVIAR e comentar
comentar = classe.find_element_by_class_name('sqdOP')

for click in range(2):
    arroba = choice(lista)
    tempo = 30
    marcar.send_keys('a', Keys.ENTER, arroba.value)
    comentar.send_keys(Keys.ENTER)
    t = localtime()  # Pegar a hora e data que esta sendo comentado
    agora = strftime("%H:%M:%S", t)
    print(f'Voce Marcou: {arroba.value} as {agora}')
    sleep(tempo)
