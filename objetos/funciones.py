import os
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from objetos.browser import driver
import time
import random
from selenium.webdriver.support.ui import Select

contador = 1
url = 'https://involveprecan.involverh.com.mx/activate-account/'
urlToken = ''


def captura(carpeta: str):
    global contador
    now = datetime.now()
    carpeta = 'imagenes/' + str(carpeta) + '/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1


def captura_time(carpeta: str, segundos):
    time.sleep(segundos)
    captura(carpeta)


def click_elemento(xpath, carpeta: str, segundos=1):
    Btnhome = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    Btnhome.click()
    captura_time(carpeta, segundos)


def borrarTexto(xpath, segundos = 1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(segundos)
    CampoNombres.clear()


def text_elemento(xpath, valor, carpeta: str, segundos=1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    captura_time(carpeta, segundos)


def text_elemento_intro(xpath, valor, carpeta: str, segundos=1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    time.sleep(1)
    CampoNombres.send_keys(Keys.ENTER)
    captura_time(carpeta, segundos)


def scrollearElemento(xpath, carpeta, segundos):
    element = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    element.location_once_scrolled_into_view
    captura_time(carpeta, segundos)


ruta = ''
def getRuta():
    imgRuta = os.getcwd().split('/')
    print(len(imgRuta))
    base = ''
    for i in range(len(imgRuta) - 2):
        print(imgRuta[i])
        base = base + str(imgRuta[i]) + '/'
    return base

def foto():
    global ruta
    baseImg = getRuta()
    imagen = random.randint(0, 11)
    print(imagen)
    ruta = (baseImg +'archivos/imgPerfil/' + str(imagen) + '.jpeg')
    print(ruta)
    return ruta


def cambio_imagen(xpath, valor, carpeta: str, segundos=2):
    perfil = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    perfil.send_keys(valor)
    time.sleep(segundos)
    captura_time(carpeta, segundos)


def comboBox(xpath, valor, carpeta: str, segundos=2):
    nombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(10)
    drop = Select(nombres)
    drop.select_by_index(valor)
    captura_time(carpeta, segundos)


def codigo(xpath, carpeta, code1, code2, code3, code4, segundos):
    Confirmacion = driver.find_element(By.XPATH, xpath)
    codigo = Confirmacion.text
    print(codigo.split(','))
    print(codigo[0])
    print(codigo[1])
    print(codigo[2])
    print(codigo[3])
    captura_time(carpeta, segundos)
    text_elemento(code1, codigo[0], carpeta, 1)
    text_elemento(code2, codigo[1], carpeta, 1)
    text_elemento(code3, codigo[2], carpeta, 1)
    text_elemento(code4, codigo[3], carpeta, 1)


rutapdf = ''
def pdfs():
    global ruta
    base= getRuta()
    pdf = ['alberto', 'carlos', 'cristian', 'daniel', 'diana', 'mario', 'octavio', 'romero']
    aleatorio = random.choice(pdf)
    print(aleatorio)
    ruta = (base + 'archivos/pdf/' + str(aleatorio) + '.pdf')
    print(ruta)
    return ruta

def pdf(xpath, valor, carpeta: str, segundos=2):
    perfil = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(2)
    driver.implicitly_wait(2)
    perfil.send_keys(valor)
    time.sleep(segundos)
    captura_time(carpeta, segundos)


def token(xpath):
    global url
    getToken = driver.find_element(By.XPATH, xpath)
    token = getToken.text
    print(url + token)
    driver.get(url + token)


def nombres(xpath, carpeta, segundos=1):
    Nombres = ['Hugo', 'Dennis', 'Miguel', 'Gabriel', 'Javi', 'Lucio', 'Jesus', 'Victor', 'Abraham', 'Juan', 'Rafeel', 'Ramiro', 'Pedro', 'Julian', 'Valentin']
    aleatorio = random.choice(Nombres)
    print(aleatorio)
    text_elemento(xpath, aleatorio, carpeta, segundos)


def apellidos(xpath, carpeta, segundos=1):
    apellido = ['Álvarez', 'Castillo', 'De León', 'Díaz', 'Espinoza', 'Fernández', 'García', 'Salazar', 'Santana',
                 'Zambrano', 'Perez', 'Rodriguez', 'Martinez', 'Garcia', 'Torres', 'Olivera', 'Lopez', 'Sanchez',
                 'Ascarragan', 'Hernandez']
    aleatorio = random.choice(apellido)
    print(aleatorio)
    text_elemento(xpath, aleatorio, carpeta, segundos)

def fechaNac(xpath, carpeta, segundos=1):

    fechas = ['1212004', '12122003', '12122002', '12122001', '12122000', '12121999', '12121998', '12121997', '12121996', '12121995'
        , '12121994', '12121993', '12121992', '13121991', '12121990', '12121989', '12121988', '12121987', '12121986', '12121985'
        , '12121984', '12121983', '12121982', '12121981', '12121980', '12121979', '12121978', '12121977', '12121976', '12121975'
        , '12121974', '12121973', '12121972', '12121971', '12121970', '12121969', '12121968', '21121967', '21121966', '21121965'
        , '21121964', '21121963', '21121962', '21121961', '21121960']
    aleatorio = random.choice(fechas)
    print(aleatorio)
    text_elemento(xpath, aleatorio, carpeta, segundos)