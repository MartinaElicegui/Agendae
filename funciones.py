from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import numpy
import csv
import os


# Crea una instancia del driver y la devuelve
def generarDriver():
    rutaDriver = os.path.join(os.getcwd(),"chromedriver")
    driver = webdriver.Chrome(rutaDriver, chrome_options=Options()) 
    Options().add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36")
    return driver

# Se loguea con usuario y contraseña en Agendae
def loguear(driver):
    driver.get('http://agendae.com.ar/')
    driver.maximize_window()
    usuario = "rosario"
    passw1 = "8dwnjt12"
    campoUsuario = encontrarElemento(driver, "campoUsuario")
    campoContraseña = encontrarElemento(driver, "campoContraseña")
    campoUsuario.send_keys(usuario)
    campoContraseña.send_keys(passw1)
    botonIngresar = encontrarElemento(driver, "botonIngresar")
    botonIngresar.click()

def encontrarElemento(driver, elemento):
    if (elemento == "campoUsuario"):
        campoUsuario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtUsuario"]'))
            )
        return campoUsuario
    if (elemento == "campoContraseña"):
        campoContraseña = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtPassword"]'))
            )
        return campoContraseña
    if (elemento == "botonIngresar"):
        botonIngresar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmdlogon"]'))
            )
        return botonIngresar
    if (elemento == "urlBanco"):
        botonIngresar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmdlogon"]'))
            )
        return botonIngresar

def navegarPorBancos (driver):
    for i in range(1,4):
        # //div[@id="mediomenucontenido"]//li[contains(.,'Tasas de Interés')]/ul/li[1]//div[1]//div[1]/a[contains(@href,'.aspx')]
        # urlBanco = driver.find_element_by_xpath("//div[@id='mediomenucontenido']//li[contains(.,'Tasas de Interés')]/ul/li[1]//div[1]//div["+str(i)+"]/a[contains(@href,'.aspx')]")
        try:
            # urlBanco = WebDriverWait(driver, 15).until(
            # EC.element_to_be_clickable((By.XPATH, "//div[@id='mediomenucontenido']//li[contains(.,'Tasas de Interés')]/ul/li["+str(i)+"]"))
            # )
            # urlBanco.click()
            # urlBanco = driver.find_element_by_xpath("//div[@id='mediomenucontenido']//li[contains(.,'Tasas de Interés')]/ul/li["+str(i)+"]")
            urlBanco = driver.find_element_by_xpath('//div[@id="mediomenucontenido"]//li[contains(.,"Tasas de Interés")]//li['+str(i)+']')
            sleep(5)
            ActionChains(driver).move_to_element(urlBanco).click(urlBanco).perform()
            urlBanco.click()
            sleep(10)
        except:
            print("No se ha encontrado la URL del banco")
        if (i == 1):
            print("Extrayendo del banco Central")
            navegarPorTasas(driver, 2)
        # if (i == 2):
        #     print("Extrayendo del banco Nación")
        #     # extraerTasas(driver,9)
        # if (i == 3):
        #     print("Extrayendo del banco de Santa Fe")
        #     extraerTasas(driver,11)

def navegarPorTasas(driver, cant):
    for i in range (1, cant):
        sleep(3)
        try:
            urlTasa = driver.find_element_by_xpath("//div[@id='mediomenucontenido']//div["+str(i)+"]//a[1]")
            print("Este es el texto contenido: ",urlTasa.text)
            urlTasa.click()
        except:
            print("No se ha encontrado la URL de la Tasa")
        sleep(2)

def volverPaginaAnterior(driver):
    driver.execute_script("window.history.go(-1)")

# El rejunte de todo
def extraerTasas(driver):
    # Selecciona la tabla entera (contenedor mayor)
    tablaCompleta = driver.find_element_by_xpath('//*[@id="divgrillalistadogeneral"]/table')
    print("ESTO ES LA TABLA COMPLETA: ")
    print(tablaCompleta)

    # Recorre la tabla y guarda cada una de sus filas en la lista filas[]. Las imprime
    filas = []
    for fila in tablaCompleta:
        print(fila.text)
        filas.append(fila.text)

    print("El tipo de elementos es: ", type(filas))
    print("La longitud de la lista es: ", len(filas))

    # size = len(filas)
    # idx_list = [idx + 1 for idx, val in enumerate(filas) if val == "/n" or val == "\n"] 
    # res = [filas[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]
  
    # # print result
    # print("The list after splitting by a value : " + str(res))

    return (filas)

# Ver el video "https://www.youtube.com/watch?v=0QHvgAcGhUc" para más info sobre la extracción de tablas
# Tiene 15 filas (las dos primeras NO interesan porque son parte del título) y 33 columnas.
def extraerTasas2(driver):
    filas = len(driver.find_elements_by_xpath('//*[@id="divgrillalistadogeneral"]/table//tbody//tr'))
    columnas = len(driver.find_elements_by_xpath('//*[@id="divgrillalistadogeneral"]/table//tbody//tr//th'))
    print("La cantidad de filas que tiene la tabla es: ", filas)
    print("La cantidad de columnas que tiene la tabla es: ", columnas)

    # for n in range(3, filas+1):
    #   for b in range (3,columnas+1):
    for n in range (3,4):
        for b in range (5,10):
            print("Posición - [",n,"][",b, "]")
            dato = driver.find_element_by_xpath('//*[@id="divgrillalistadogeneral"]/table//tbody/tr["+str(n)"]//td["+str(b)"]')
            print(dato)
            print(dato.text, end = "  -  ")
    
    uno = driver.find_element_by_xpath('//*[@id="divgrillalistadogeneral"]/table//tbody/tr[2]//td[2]').text
    print("Este es el elemento UNO: ", uno)

    
def escribirEnArchivo(tablaFinal):
    with open('tasas.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter = ',', lineterminator='\n')
            writer.writerow(tablaFinal)