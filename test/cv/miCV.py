import time

from objetos.browser import driver
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido
from objetos.funciones import click_elemento, scrollearElemento
from objetos.cv.miCV.Obj_videoPresentacion import grabar, masTarde, continuar, pregunta1, pregunta2, pregunta3, \
    pregunta4, iniciarGrabacion, siguientePregunta, detener, reiniciar, guardar

def miCv():
    try:
        loginValido()

        time.sleep(1)
        carpeta = 'miCV'
        scrollearElemento(grabar, carpeta, 2)
        click_elemento(grabar, carpeta, 2)

        click_elemento(continuar, carpeta, 1)
        click_elemento(pregunta1, carpeta, 1)
        click_elemento(pregunta2, carpeta, 1)
        click_elemento(continuar, carpeta, 1)

        click_elemento(iniciarGrabacion, carpeta, 2)
        time.sleep(4)
        click_elemento(siguientePregunta, carpeta, 2)
        click_elemento(detener, carpeta, 2)
        click_elemento(reiniciar, carpeta, 2)

        click_elemento(iniciarGrabacion, carpeta, 2)
        time.sleep(4)
        click_elemento(siguientePregunta, carpeta, 2)
        click_elemento(detener, carpeta, 2)
        click_elemento(guardar, carpeta, 2)

        scrollearElemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)

        print('ya paso el CV')
        return 'ya paso la sección del CV correctamente'
    except Exception as e:
        print('no pasop el CV', str(e))
        return 'no paso la sección del CV'


