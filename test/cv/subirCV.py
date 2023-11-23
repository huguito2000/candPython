import time
from objetos.cv.miCV.Obj_subirCV import agregar, cv, regresar, rutaPDF
from objetos.funciones import pdf, scrollearElemento, click_elemento
from test.login import loginValido
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion

def subirPDF():
    try:
        carpeta = 'subirPDF'
        loginValido()
        print('ruta del archivo' + rutaPDF)
        time.sleep(1)
        scrollearElemento(agregar, carpeta, 2)
        click_elemento(agregar, carpeta, 1)
        click_elemento(regresar, carpeta, 2)
        time.sleep(1)
        scrollearElemento(agregar, carpeta, 2)
        click_elemento(agregar, carpeta, 1)
        time.sleep(1)
        pdf(cv, rutaPDF, carpeta, 2)
        click_elemento(regresar, carpeta, 2)
        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se sube correctamente el PDF')
        return 'Se sube correctamente el PDF'
    except Exception as e:
        print('no se sube el PDF', str(e))
        return 'no se subio el pdf'