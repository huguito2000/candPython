from test.login import loginValido
from selenium.webdriver.common.by import By
from objetos.browser import driver
from objetos.funciones import text_elemento, click_elemento, comboBox, cambio_imagen,pdf,nombres, apellidos, fechaNac
from objetos.registro.obj_informacion1 import subirCV, nombre1, nombre2, apellidoP, apellidoM, fecha, nacionalidad, \
    edoCivil, genero, siguiente


import random
import time



loginValido()
carpeta = 'informacion'
time.sleep(3)

nombres(nombre1, carpeta, 1)
nombres(nombre2, carpeta, 1)
apellidos(apellidoP, carpeta, 2)
apellidos(apellidoM, carpeta, 2)
fechaNac(fecha, carpeta, 2)
comboBox(nacionalidad, 1, carpeta, 1)
time.sleep(1)
comboBox(edoCivil, 1, carpeta, 2)
time.sleep(1)
comboBox(genero, 2, carpeta, 2)
time.sleep(1)
click_elemento(siguiente, carpeta, 2)
