import random
import time

from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido
from objetos.busqueda.obj_filtros import misVancates
from objetos.funciones import click_elemento, text_elemento, comboBox, scrollearElemento
from objetos.busqueda.obj_postulacion import busqueda, postulaciones, continuarProceso, vacante, postularme, empecemos, \
    ExpL1, ExpL2, ExpL3Si, ExpL3No, siguienteEL1, CbHD, HD2, HBSi, HBNo, continuarVE, iniciar, detener, guardar



def experiencia(a: int, b: int):
    exp = random.randint(a, b)
    return exp

def postulacionCorrecta():
    try:
        loginValido()

        carpeta = 'postulacion'
        click_elemento(misVancates, carpeta,2)
        click_elemento(vacante, carpeta, 2)
        click_elemento(postularme, carpeta, 2)
        click_elemento(empecemos, carpeta, 2)

        exp = experiencia(1, 30)
        text_elemento(ExpL1, exp, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)

        exp = experiencia(1, 30)
        text_elemento(ExpL2, exp, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)

        click_elemento(ExpL3Si, carpeta, 2)
        click_elemento(ExpL3No, carpeta, 2)
        click_elemento(ExpL3Si, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)

        comboBox(CbHD, 4, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)

        exp = experiencia(1, 30)
        text_elemento(HD2, exp, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)

        click_elemento(HBSi, carpeta, 2)
        click_elemento(HBNo, carpeta, 2)
        click_elemento(HBSi, carpeta, 2)
        click_elemento(siguienteEL1, carpeta, 2)
        time.sleep(2)

        click_elemento(continuarVE, carpeta, 2)
        click_elemento(iniciar, carpeta, 2)
        time.sleep(15)
        click_elemento(detener, carpeta, 2)
        click_elemento(guardar, carpeta, 2)

        scrollearElemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)

        print('se postulo correctamente')
        return 'Se realizo la postulacion correctamente'
    except Exception as e:
        print('no se hizo la postulacion', str(e))
        return 'No se realizo la postulacion'

postulacionCorrecta()