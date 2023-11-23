import time
from objetos.cv.miCV.obj_habilidadesDuras import agregar, habilidad, nivel, regresar, add, regresar2
from objetos.funciones import text_elemento_intro, comboBox, click_elemento
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido

def habDuras():
    try:
        carpeta = 'habilidadDura'
        loginValido()

        click_elemento(agregar, carpeta, 1)
        time.sleep(2)
        click_elemento(regresar, carpeta, 1)
        click_elemento(agregar, carpeta, 1)
        time.sleep(2)
        text_elemento_intro(habilidad, 'excel', carpeta, 1)
        comboBox(nivel, 4, carpeta, 1)
        click_elemento(add, carpeta, 1)
        time.sleep(1)
        click_elemento(regresar2, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se agrego la habilidad dura')
        return 'se agrego la habilidad dura'
    except Exception as e:
        print('no paso la habilidad dura', str(e))
        return 'no paso la habilidad dura'





