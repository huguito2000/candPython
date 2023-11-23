import time

from objetos.cv.miCV.Obj_idioma import agregar, idioma, nivel, regresar, add
from objetos.funciones import comboBox, click_elemento, scrollearElemento
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido

def addIdioma():
    try:
        carpeta = 'idioma'
        loginValido()
        time.sleep(1)
        scrollearElemento(agregar, carpeta, 1)
        click_elemento(agregar, carpeta, 1)
        click_elemento(regresar, carpeta, 1)
        time.sleep(1)
        scrollearElemento(agregar, carpeta, 1)
        time.sleep(1)
        click_elemento(agregar, carpeta, 1)
        comboBox(idioma, 1, carpeta, 1)
        comboBox(nivel, 4, carpeta, 1)
        click_elemento(add, carpeta, 2)
        click_elemento(regresar, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('Se agrego el idioma')
        return 'Se agrego el idioma'
    except Exception as e:
        print('No se agrego el idioma', str(e))
        return 'No se agrego el idioma'