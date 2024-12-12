
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import keyboard
import time
import canales
import teclas

def inicializarDriver():
    # Ruta de la extensión uBlock para Firefox
    uBlockExtensionPATH = "uBlock.xpi"  # Por defecto lo busca en la misma carpeta

    # Opciones de Firefox
    options = Options()
    options.add_argument("--kiosk") 
    
    # Inicializar el controlador de Firefox
    driverFirefox = webdriver.Firefox(options=options)
    
    # Deshabilitar las restricciones de reproducción automática
    options.set_preference("media.autoplay.default", 1)  # Permitir la reproducción automática de medios
    options.set_preference("media.autoplay.allow-muted", True)  # Permitir la reproducción automática de videos silenciados
    
    # Instalar la extensión de uBlock
    driverFirefox.install_addon(uBlockExtensionPATH, temporary=True)

    return driverFirefox

def cambiarCanal(navegador, urlCanal):
    # Sale de la pantalla completa anterior
    print("Saliendo de pantalla completa.")
    actions = ActionChains(navegador)
    actions.send_keys("f").perform()

    # Navega al canal
    print("Cambio de canal.")
    navegador.get(urlCanal)

    # Le da unos segundos a cargar
    print("Esperando que cargue")
    time.sleep(5)

    # Vuelve a pantalla completa
    print("Entrando a pantalla completa")
    actions.send_keys("f").perform()

def main():
    

    # Inicializa el driver
    print("Iniciando instancia del navegador.")
    driver = inicializarDriver()

    # Navegar al canal por defecto
    print("Cambiando al canal por defecto.")
    cambiarCanal(driver, canales.canal1)

    # Bucle infinito
    continuar = True
    while continuar:
        #Chequear si hay que pasar al canal 1
        if keyboard.is_pressed(teclas.teclaCanalUno):
            print(f"Tecla {teclas.teclaCanalUno} presionada, cambiando al canal 1...")
            cambiarCanal(driver, canales.canal1)
            
        #Chequear si hay que pasar al canal 2
        elif keyboard.is_pressed(teclas.teclaCanalDos):
            print(f"Tecla {teclas.teclaCanalDos} presionada, cambiando al canal 2...")
            cambiarCanal(driver, canales.canal2)
        #Chequear si hay que pasar al canal 3
        elif keyboard.is_pressed(teclas.teclaCanalTres):
            print(f"Tecla {teclas.teclaCanalTres} presionada, cambiando al canal 3...")
            cambiarCanal(driver, canales.canal3)

        #Chequear si hay que terminar el programa
        elif keyboard.is_pressed(teclas.teclaFin):
            print("Tecla 0 presionada, finalizando programa...")
            continuar = False
        
        # Pausa breve para evitar usar demasiados recursos
        time.sleep(0.1)
    
    # Cerrar el navegador
    driver.close()
    print("Fin del programa.")


if __name__ == "__main__":
    main()
