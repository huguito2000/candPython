import time
from objetos.cv.obj_mis_datos import perfil
from objetos.funciones import click_elemento, text_elemento, comboBox, scrollearElemento
from objetos.cv.miCV.Obj_expLaboral import agregar, puesto, tipoPuesto, empresa, fecha, si, no, genteSi, genteNo, humanos, funciones, cancelar, guardar
from objetos.obj_login import cerrarSesion
from test.login import loginValido

def experienciaLaboral():
    try:
        carpeta = 'expLaboral'
        loginValido()
        click_elemento(agregar, carpeta, 1)
        click_elemento(cancelar, carpeta, 2)
        click_elemento(agregar, carpeta, 1)
        text_elemento(puesto, 'lider', carpeta, 1)
        comboBox(tipoPuesto,7, carpeta, 1)
        text_elemento(empresa, 'involve', carpeta, 1)
        text_elemento(fecha, '12122000', carpeta, 1)
        click_elemento(si, carpeta, 1)
        click_elemento(no, carpeta, 1)
        click_elemento(si, carpeta, 1)
        click_elemento(genteSi, carpeta, 1)
        click_elemento(genteNo, carpeta, 1)
        click_elemento(genteSi, carpeta, 1)
        text_elemento(humanos, '3', carpeta, 1)
        text_elemento(funciones, 'hacer todo lo que se pueda', carpeta, 1)
        click_elemento(guardar, carpeta, 1)

        scrollearElemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        print('se edita la experiencia laboral')
        return 'se edita ña experiencia lboral'
    except Exception as e:
        print('No se edita la experiencia laboral', str(e))
        return 'No se edita la experiencia laboral'

