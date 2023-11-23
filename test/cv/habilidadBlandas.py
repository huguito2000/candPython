import time

from objetos.cv.miCV.obj_HabilidadBlandas import agregar, habilidad, regresar, regresar2
from objetos.funciones import click_elemento, text_elemento_intro
from objetos.obj_login import cerrarSesion
from objetos.cv.obj_mis_datos import perfil
from test.login import loginValido

def habBlanda():
    try:
        carpeta = 'habBlanda'

        loginValido()
        time.sleep(2)
        click_elemento(agregar, carpeta, 1)
        time.sleep(2)
        click_elemento(regresar, carpeta, 1)
        click_elemento(agregar, carpeta, 1)
        text_elemento_intro(habilidad, 'trabajo en equipo', carpeta, 1)
        time.sleep(1)
        click_elemento(regresar2, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('Se agrega la habilidad blanda')
        return 'se agrega la habilidad blanda'
    except Exception as e:
        print('No se agrego la habilidad blanda')
        return ' No se agrego la habilidad blanda'



