import time

from objetos.funciones import click_elemento, text_elemento, comboBox
from objetos.cv.miCV.Obj_nivelEducativo import agregar, nivelEducativo, titulo, institucion, estatus, inicioYear, finYear, cancelar, guardar
from test.login import loginValido
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion

def nivelEducacion():
    try:
        carpeta = 'educacion'
        loginValido()
        time.sleep(1)
        click_elemento(agregar, carpeta, 1)
        click_elemento(cancelar, carpeta, 1)
        click_elemento(agregar, carpeta, 1)
        comboBox(nivelEducativo,7, carpeta, 1)
        text_elemento(titulo, 'ingeniero', carpeta, 1)
        text_elemento(institucion, 'unam', carpeta, 1)
        comboBox(estatus, 4, carpeta, 1)
        text_elemento(inicioYear, '2000', carpeta, 1)
        text_elemento(finYear, '2005', carpeta, 1)
        click_elemento(guardar, carpeta, 1)
        time.sleep(1)
        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se agrega el nievel de educación')
        return 'se agregar el nivel de educacion'
    except Exception as e:
        print('no se agregar el nivel de educaciuón', str(e))
        return 'no se agregar el nivel de educaciuón'

nivelEducacion()