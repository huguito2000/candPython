import time

from objetos.cv.miCV.Obj_areaExperiencia import agregar, area, especialidad, regresar, aceptar
from objetos.funciones import comboBox, click_elemento
from test.login import loginValido
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion

def areaExperiencia():
    try:
        carpeta = 'areaExp'

        loginValido()
        click_elemento(agregar, carpeta, 1)
        click_elemento(regresar, carpeta, 1)
        time.sleep(1)
        click_elemento(agregar, carpeta, 1)
        time.sleep(1)
        comboBox(area, 2, carpeta, 1)
        comboBox(especialidad, 1, carpeta, 1)
        click_elemento(aceptar, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se agrego la experiencia laboral')
        return 'se agrego la experiencia laboral'
    except Exception as e:
        print('No se agrego la experiencia laboral')
        return 'No se agrego la experiencia laboral'

