import time
import requests
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup




usuario = "rosario"
passw1 = "8dwnjt12"

driver = webdriver.Chrome()
driver.get('http://www.agendae.com.ar/default.aspx')
time.sleep(2)

mbox = driver.find_element_by_xpath('//*[@id="txtUsuario"]')


mbox.send_keys(usuario) #pone usuario
mbox = driver.find_element_by_xpath('//*[@id="txtPassword"]')
mbox.send_keys(passw1) #pone usuario

driver.find_element_by_xpath('//*[@id="cmdlogon"]').click()
#click para ingresar
time.sleep(2)
driver.find_element_by_xpath('//*[@id="refbco3"]').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="mediomenucontenido"]/ul/li[1]/ul/li[3]/div/div[1]/a').click()

table_header = driver.find_elements_by_xpath('//*[@id="divgrillalistadogeneral"]/table')



# header_row = []
# for header in table_header:
#     header_row.append(header.text)

# print(header_row)

##table_data = driver.find_elements_by_xpath('//*[@id="ContenidoDentroDeMaster_gridListado"]/tbody/tr[2]')
table_data = driver.find_elements_by_xpath('./th')

for row in table_data:
    columns = row.find_elements_by_xpath('./td') # Use dot in the xpath to find elements with in element.
    table_row = []
    for column in columns:
        table_row.append(column.text)
    print(table_row)

input('Presione cualquier tecla para continuar.......')