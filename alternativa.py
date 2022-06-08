import sys
from funciones import *

def main(): 
    driver = generarDriver()
    loguear(driver)
    # BCRA Tasa pasiva capitalizada
    driver.get("http://agendae.com.ar/listado.aspx?t=2")
    extraerTasas2(driver)
    # dividirLista(driver, tablaFinal)
    # escribirEnArchivo(tablaFinal)
       
    input("Presione una tecla para terminar.")
    
if __name__ == "__main__":
    sys.exit(main())