from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
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

def navegarPorTasas (driver):
    for i in range(4):
        # //div[@id="mediomenucontenido"]//li//li[i] (i = 1,2,3,4)
        urlBanco = driver.find_element_by_xpath("//div[@id='mediomenucontenido']//li//li[i]")
        urlBanco.click()
        driver.back()
        sleep(2)
